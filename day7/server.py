# pip install flask_restful
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import cx_Oracle
import pandas as pd
conn = cx_Oracle.connect('java','oracle','localhost:1521/xe')
sql = {"select_subject": """ SELECT * FROM 과목 WHERE 과목번호 = :1"""}
app = Flask(__name__)
CORS(app)
api = Api(app)
todos = {}
seq = 1
class TodoResource(Resource):
    # 조회
    def get(self, subject_id):
        print(subject_id)
        df = pd.read_sql(con=conn, sql=sql['selec_subject'], params=[subject_id])
        print(df['과목이름'][0])
        if len(df) > 0:
            return {subject_id : df['과목이름'][0],'학점':df['학점'][0]}
        else:
            return {"error" : "Todo not found"}, 404
    # 생성
    def post(self):
        global seq
        todo_id = seq
        todos[todo_id] = request.form['data']
        seq += 1
        return {todo_id: todos[todo_id]}, 200
    # 수정
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id : todos[todo_id]}

    # 삭제
    def delete(self, todo_id):
        if todo_id in todos:
            del todos[todo_id]
            return {"result": "Todo deleted"}, 200
        else:
            return {"error": "Todo not found"}, 404
api.add_resource(TodoResource,'/subject', '/subject/<int:subject_id>')
if __name__ == '__main__':
    app.run(debug=True)
