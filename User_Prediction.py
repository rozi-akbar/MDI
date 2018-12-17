import pyodbc
import sklearn as skl
import matplotlib.pyplot as plt

conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-07HJR0C;Database=db_final;Trusted_Connection=yes;')
cursor = conn.cursor()
fak = []
value = []
value2 = []
value3 = []
value4 = []
value5 = []
value6 = []

cursor.execute("SELECT MONTH(tanggal) MONTH, COUNT(*) as 'Jumlah Access' FROM MHS WHERE YEAR(tanggal) = '2013' GROUP BY MONTH(tanggal) ORDER BY MONTH(tanggal)")
for row in cursor.fetchall():
    fak.append(int(row[0]))
    value.append(int(row[1]))

cursor.execute("SELECT MONTH(tanggal) MONTH, COUNT(*) as 'Jumlah Access' FROM MHS WHERE YEAR(tanggal) = '2014' GROUP BY MONTH(tanggal) ORDER BY MONTH(tanggal)")
for row2 in cursor.fetchall():
    value2.append(int(row2[1]))

cursor.execute("SELECT MONTH(tanggal) MONTH, COUNT(*) as 'Jumlah Access' FROM MHS WHERE YEAR(tanggal) = '2015' GROUP BY MONTH(tanggal) ORDER BY MONTH(tanggal)")
for row3 in cursor.fetchall():
    value3.append(int(row3[1]))

cursor.execute("SELECT MONTH(tanggal) MONTH, COUNT(*) as 'Jumlah Access' FROM MHS WHERE YEAR(tanggal) = '2016' GROUP BY MONTH(tanggal) ORDER BY MONTH(tanggal)")
for row4 in cursor.fetchall():
    value4.append(int(row4[1]))

cursor.execute("SELECT MONTH(tanggal) MONTH, COUNT(*) as 'Jumlah Access' FROM MHS WHERE YEAR(tanggal) = '2017' GROUP BY MONTH(tanggal) ORDER BY MONTH(tanggal)")
for row5 in cursor.fetchall():
    value5.append(int(row5[1]))

cursor.execute("SELECT MONTH(tanggal) MONTH, COUNT(*) as 'Jumlah Access' FROM MHS WHERE YEAR(tanggal) = '2018' GROUP BY MONTH(tanggal) ORDER BY MONTH(tanggal)")
for row6 in cursor.fetchall():
    value6.append(int(row6[1]))

plt.scatter(fak,value)
plt.scatter(fak,value2)
plt.scatter(fak,value3)
# plt.plot(fak,value4)
# plt.plot(fak,value5)
# plt.plot(fak,value6)

plt.show()