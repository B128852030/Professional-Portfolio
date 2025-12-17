import sqlite3
import pandas as pd
import os

# Step 1: Build absolute path to CSV (relative to script location)
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "sales.csv")
print("Loading CSV from:", csv_path)

# Step 2: Load CSV
df = pd.read_csv(csv_path)
print("CSV loaded successfully!")
print("Rows loaded:", len(df))

# Step 3: Connect to SQLite database (creates sales.db in python folder)
db_path = os.path.join(os.path.dirname(__file__), "sales.db")
conn = sqlite3.connect(db_path)

# Step 4: Write data to SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data written to database successfully!")

# Step 5: Close connection
conn.close()
