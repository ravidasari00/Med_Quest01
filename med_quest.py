import pyodbc as pd
import pandas as p
conn=pd.connect(server="183.82.111.187",
                database="SIRI_UAT",
                user="sa",
                password="Inc0rrect",
                driver="{ODBC Driver 17 for SQL Server}")
print(conn)
cursor=conn.cursor()
sql="""
select PtMt_Patient_Code,PtMt_Patient_Name,PtMt_Patient_Sex_Code,PtMt_Patient_Age,PtMt_Patient_Age_Type,
PtMt_Patient_Second_Age,PtMt_Patient_Second_Age_Type,PtMt_Patient_Mobile_Number,PtMt_Patient_Email_ID,
PtMt_Patient_Reg_Date,PtMt_Patient_Edit_Date,PtMt_Patient_Created_date from Lb_PtMt_Patient_Mast_T
"""
#A cursor is an object which helps to execute the query and fetch the records from the database
cursor.execute(sql)
rows=cursor.fetchall()
for row in rows:
    print(row)
#read SQL query into DataFrame
data=p.read_sql_query(sql,conn)
df=p.DataFrame(data)
#save the DataFrame to Excel Sheet
datatoexcel = p.ExcelWriter('Patient_Data01.xlsx')
df.to_excel(datatoexcel)
datatoexcel.save()