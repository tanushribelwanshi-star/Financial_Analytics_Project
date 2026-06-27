import sqlite3
import pandas as pd

# Connect to database
connection = sqlite3.connect("complaints.db")

# SQL Query

query = """
SELECT
strftime('%Y-%m', [Date received]) AS Month,
COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY Month
ORDER BY Month;
"""

# Execute query
result = pd.read_sql_query(query, connection)

# Print result
print(result)

# Close connection
connection.close()