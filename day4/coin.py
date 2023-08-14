import requests
import json
url = 'https://api.upbit.com/v1/market/all'
res = requests.get(url)
json_data = json.loads(res.text)
print(json_data)
for row in json_data:
    print(row['market'], row['korean_name'], row['english_name'])
import sqlite3
conn = sqlite3.connect('stock.db')
sql = """
    INSERT INTO stock VALUES('APPL', '애플', 'apple')
    """
cur = conn.cursor()
cur.execute(sql)
