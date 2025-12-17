import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1️⃣ Connect to SQLite database
db_path = os.path.join(os.path.dirname(__file__), "sales.db")
conn = sqlite3.connect(db_path)

# 2️⃣ Query: Total revenue per product
df_products = pd.read_sql_query("""
    SELECT product, SUM(quantity * price) AS total_revenue
    FROM sales
    GROUP BY product
    ORDER BY total_revenue DESC;
""", conn)

# 3️⃣ Query: Sales by region
df_region = pd.read_sql_query("""
    SELECT region, SUM(quantity * price) AS total_revenue
    FROM sales
    GROUP BY region
    ORDER BY total_revenue DESC;
""", conn)

# 4️⃣ Query: Monthly sales trends
df_monthly = pd.read_sql_query("""
    SELECT strftime('%Y-%m', order_date) AS month, SUM(quantity * price) AS monthly_revenue
    FROM sales
    GROUP BY month
    ORDER BY month;
""", conn)

# Close DB connection
conn.close()

# 5️⃣ Plot: Revenue per Product
plt.figure(figsize=(8,5))
plt.bar(df_products['product'], df_products['total_revenue'], color='skyblue')
plt.title("Total Revenue per Product")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.show()

# 6️⃣ Plot: Revenue by Region
plt.figure(figsize=(6,4))
plt.pie(df_region['total_revenue'], labels=df_region['region'], autopct='%1.1f%%', startangle=140)
plt.title("Revenue by Region")
plt.tight_layout()
plt.show()

# 7️⃣ Plot: Monthly Sales Trend
plt.figure(figsize=(8,5))
plt.plot(df_monthly['month'], df_monthly['monthly_revenue'], marker='o', color='green')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
