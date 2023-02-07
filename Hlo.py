import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-G1E137K\MSSQLSERVER01;'
                    'Database=class;'
                    'Trusted_Connection=yes;')
cursor = conn.cursor()

cursor.execute('select * from emp1')
for row in cursor:
    print(row)