import pandas as pd
import cx_Oracle
conn = cx_Oracle.connect("java","oracle","localhost:1521/xe")
df = pd.read_sql(con= conn, sql="SELECT * FROM member")
print(df.head())
print(df.describe())
wrtier = pd.ExcelWriter("member.xlsx", engine="xlsxwriter")
df.to_excel(wrtier, sheet_name="sheet1")
wrtier.close()
# pip install xlsxwriter