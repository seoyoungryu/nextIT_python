# pip install cx_Oracle
import cx_Oracle
conn = cx_Oracle.connect('java', 'oracle', 'localhost:1521/xe')
print(conn.version)
nm = input("검색할 이름을 입력해주세요:")
param = {"nm": nm}
with conn:
    cur = conn.cursor()
    sql = """
        SELECT * 
        FROM member 
        WHERE mem_name LIKE '%'||:nm||'%'
    """ #member 테이블에서 이름으로 회원 정보를 조회하는 쿼리 (like 사용)
    rows = cur.execute(sql, param)
    for r in rows:
        print(r)