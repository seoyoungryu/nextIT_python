import sqlite3
conn = sqlite3.connect('stock.db')
# insert 방법 3가지
sql = """
    INSERT INTO stock VALUES('APPL', '애플', 'apple')
    """
cur = conn.cursor()
cur.execute(sql)
# 순서 매핑
sql1 = """
    INSERT INTO stock VALUES(?,?,?)
"""
cur.execute(sql1, ['TSLA', '테슬라', 'tesla'])
# 이름 매핑
data = {'code': 'GOOGL', 'nm': '구글', 'en_nm': 'google'}
sql2 = """INSERT INTO stock VALUES(:code, :nm, :en_nm)"""
cur.execute(sql2, data)
conn.commit()
conn.close()
