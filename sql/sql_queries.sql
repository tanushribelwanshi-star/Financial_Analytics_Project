"product"
"""SELECT Product,
       COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY Product
ORDER BY Complaint_Count DESC;"""

"top 10 company"
query = """
SELECT Company,
       COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY Company
ORDER BY Complaint_Count DESC
LIMIT 10;
"""
"top state"
query = """
SELECT State,
       COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY State
ORDER BY Complaint_Count DESC
LIMIT 10;
"""

"Complaint Submission Channels"
query = """
SELECT [Submitted via],
       COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY [Submitted via]
ORDER BY Complaint_Count DESC;
"""
'''monthly trend'''
query = """
SELECT
strftime('%Y-%m', [Date received]) AS Month,
COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY Month
ORDER BY Month;
"""
'''Query 6 – Timely Response'''
'''SELECT
[Timely response?],
COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY [Timely response?];'''

'''Top Product + State Combination'''
'''SELECT
Product,
State,
COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY Product, State
ORDER BY Complaint_Count DESC
LIMIT 10;'''