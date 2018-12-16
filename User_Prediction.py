import pyodbc
import dateparser as dp
import matplotlib.pyplot as plt

conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-07HJR0C;Database=db_final;Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("select * from dbo.MHS")

for row in cursor.fetchall():
    print(row)