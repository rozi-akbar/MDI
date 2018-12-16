import pyodbc
import matplotlib.pyplot as plt
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-07HJR0C;Database=datashareits;Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("select substring(Last_AccessDsn,1,len(LEFT(Last_AccessDsn,charindex(',',Last_AccessDsn)-0))-1) as AccessDay, COUNT(Last_AccessDsn) as JumlahAccess from datashareits.dbo.Dosen group by substring(Last_AccessDsn,1,len(LEFT(Last_AccessDsn,charindex(',',Last_AccessDsn)-0))-1)")

day = []
value = []

for row in cursor.fetchall():
    print(row)
    day.append(str(row[0]))
    value.append(int(row[1]))

plt.figure(1, figsize=(7, 5))
plt.bar(day, value)
plt.suptitle('Lecture Access Categorical by Day')

for i, v in enumerate(value):
    plt.text(i-.25, v/value[i]+100, value[i], fontsize=9, color='white')

plt.show()
