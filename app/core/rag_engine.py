import os
import duckdb
from openai import OpenAI
from dotenv import load_dotenv
# Avoiod repeat questions by cache
from aiocache import cached

project_root = os.path.dirname(os.path.abspath(__file__))

env_path = os.path.join(project_root, ".env")
load_dotenv(env_path)

DB_PATH = os.path.join(project_root, "data", "enterprise_local.db")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@cached(ttl=600) # Cache the result for 600 seconds (10 mins)
def ask_ai(question):
    system_prompt = """
    You are a SQL expert for a Sales database. 
    TABLE: 'sales' (id, product, revenue, region)
    
    VALID VALUES:
    - Products: 'GenAI Agent', 'Data Connector', 'Cloud Storage'
    - Regions: 'North', 'South', 'East', 'West'
    
    RULES:
    1. For string filters, ALWAYS use LOWER() for robustness.
    2. Return ONLY the SQL code. No markdown (no ```), no explanation.
    3. End with a semicolon (;).
    
    EXAMPLE:
    Q: "Total revenue for North?"
    A: SELECT SUM(revenue) FROM sales WHERE LOWER(region) = 'north';
    """

    # 3. Call GPT-4o-mini
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Write SQL for: {question}"}
        ],
        temperature=0 
    )
    
    sql = response.choices[0].message.content.strip()
    # Clean up markdown if present
    sql = sql.replace("```sql", "").replace("```", "").strip()
    
    print(f" OpenAI Generated SQL: {sql}")
    
    # 4. Execute against DuckDB
    # Use read_only=True here so it doesn't accidentally create a new empty DB
    with duckdb.connect(DB_PATH, read_only=True) as con:
        result = con.execute(sql).fetchall()
        return result

if __name__ == "__main__":
    query = "What is the total revenue for the GenAI Agent?"
    try:
        data = ask_ai(query)
        print(f" Database Result: {data}")
    except Exception as e:
        print(f" Error: {e}")


#print(f"Tokens Used: {response.usage.total_tokens}")
