import pandas as pd
import FinanceDataReader as fdr
# pip install openpyxl
df = pd.read_excel("member.xlsx",sheet_name="sheet1", engine="openpyxl")

print(df.info())
for i, v in df.iterrows():
     print(i)
     print(v['MEM_NAME'])

samsung_2022 = fdr.DataReader('005930', '2022-01-01', '2022-12-31')
print(samsung_2022.head())
writer = pd.ExcelWriter('samsung2022.xlsx', engine="xlsxwriter")
samsung_2022.to_excel(writer, sheet_name='sheet1')
writer.close()