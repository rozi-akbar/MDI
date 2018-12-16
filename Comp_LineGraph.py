import pyodbc
import matplotlib.pyplot as plt
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-07HJR0C;Database=datashareits;Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("select Fakultas, COUNT(Fakultas) from Dosen group by Fakultas")

fak1 = []
value1 = []
fak2 = []
value2 = []

for row1 in cursor.fetchall():
    print(row1)
    fak1.append(str(row1[0]))
    value1.append(int(row1[1]))

cursor.execute("select FakultasMhs, COUNT(FakultasMhs) from Mahasiswa group by FakultasMhs")
for row2 in cursor.fetchall():
    print(row2)
    fak2.append(str(row2[0]))
    value2.append(int(row2[1]))

plt.barh(fak2,value2)
plt.barh(fak1,value1)

plt.suptitle('Comparison of ShareITS user Categorize by Faculty')

for i, v in enumerate(value1):
    plt.text(v + 3, i + .25, str(v), color='blue', va='center', fontweight='bold')

for i, v in enumerate(value2):
    plt.text(v + 3, i + .25, str(v), color='black', fontweight='bold')

plt.show()