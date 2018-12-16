import pyodbc
import matplotlib.pyplot as plt
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-07HJR0C;Database=datashareits;Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("select substring(Last_AccessDsn,1,len(LEFT(Last_AccessDsn,charindex(',',Last_AccessDsn)-0))-1) as AccessDay, COUNT(Last_AccessDsn) as JumlahAccess from datashareits.dbo.Dosen group by substring(Last_AccessDsn,1,len(LEFT(Last_AccessDsn,charindex(',',Last_AccessDsn)-0))-1)")

fak1 = []
value1 = []
fak2 = []
value2 = []

for row1 in cursor.fetchall():
    print(row1)
    fak1.append(str(row1[0]))
    value1.append(int(row1[1]))

cursor.execute("select substring(Last_AccessMhs,1,len(LEFT(Last_AccessMhs,charindex(',',Last_AccessMhs)-0))-1) as AccessDay, COUNT(Last_AccessMhs) as JumlahAccess from Mahasiswa group by substring(Last_AccessMhs,1,len(LEFT(Last_AccessMhs,charindex(',',Last_AccessMhs)-0))-1 )")
for row2 in cursor.fetchall():
    print(row2)
    fak2.append(str(row2[0]))
    value2.append(int(row2[1]))

plt.bar(fak2,value2)
plt.bar(fak1,value1)

plt.suptitle('Comparison of ShareITS user Categorize by Day')

for i, v in enumerate(value1):
    plt.text(i-.25, v/value1[i]+100, value1[i], fontsize=9, color='black')

for i, v in enumerate(value2):
    plt.text(i-.25, v/value2[i]+500, value2[i], fontsize=9, color='white')

plt.show()