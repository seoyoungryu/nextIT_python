# pip install -U finance-datareader
import FinanceDataReader as fdr
df_krx = fdr.StockListing('KRX')
df_nasdaq = fdr.StockListing('NASDAQ')

print(df_krx.head())
print(df_nasdaq.head())
samsung = fdr.DataReader('005930')
print(samsung.head())
# 그래프 그려주는 라이브러리(matplotlib)
# pip install matplotlib
import matplotlib.pyplot as plt
samsung['Close'].plot()
plt.show()