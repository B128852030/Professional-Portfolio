import sqlite3
import pandas as pd
import os

# 1️⃣ Path to SQLite database
db_path = os.path.join(os.path.dirname(__file__), "sales.db")
conn = sqlite3.connect(db_path)

# 2️⃣ Queries to run
queries = {
    "Total revenue per product": """
        SELECT product, SUM(quantity * price) AS total_revenue
        FROM sales
        GROUP BY product
        ORDER BY total_revenue DESC;
    """,
    "Top customers by spending": """
        SELECT customer, SUM(quantity * price) AS total_spent
        FROM sales
        GROUP BY customer
        ORDER BY total_spent DESC;
    """,
    "Sales by region": """
        SELECT region, SUM(quantity * price) AS total_revenue
        FROM sales
        GROUP BY region
        ORDER BY total_revenue DESC;
    """,
    "Monthly sales trends": """
        SELECT strftime('%Y-%m', order_date) AS month, SUM(quantity * price) AS monthly_revenue
        FROM sales
        GROUP BY month
        ORDER BY month;
    """
}

# 3️⃣ Execute queries and print results
for title, query in queries.items():
    print("\n=== ", title, " ===")
    df = pd.read_sql_query(query, conn)
    print(df)

# 4️⃣ Close connection
conn.close()
