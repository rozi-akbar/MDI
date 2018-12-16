import pyodbc
import matplotlib.pyplot as plt
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-07HJR0C;Database=datashareits;Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("select Fakultas, COUNT(Fakultas) from Dosen group by Fakultas")

fak = []
value = []

for row in cursor.fetchall():
    print(row)
    fak.append(str(row[0]))
    value.append(int(row[1]))

plt.figure(1, figsize=(15, 5))

plt.barh(fak, value, color = 'purple')
plt.suptitle('Lecture Access Categorical by Faculty')

for i, v in enumerate(value):
    plt.text(v + 3, i + .25, str(v), color='blue', va='center', fontweight='bold')

plt.show()