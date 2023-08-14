import json
import requests
import cx_Oracle

def fn_stock_get():
    conn =cx_Oracle.connect("java","oracle","localhost:1521/xe")
    sql = """
        INSERT INTO tb_stock (itemCode, stockName, closePrice)
        VALUES (:1,:2,:3)
    """
    for i in range(1, 100):
        print(i, "="*100)
        url="https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={0}&pageSize=50".format(str(i))
        res = requests.get(url)

        if res.status_code == 200:
            data = json.loads(res.content)
            print(data['stocks'])
            if len(data['stocks']) == 0:
                break
            for idx, val in enumerate(data['stocks']):
                cur = conn.cursor()
                cur.execute(sql, [val['itemCode'], val['stockName'], val['closePrice']])
                conn.commit()
    conn.close()
if __name__ == '__main__':
    fn_stock_get()