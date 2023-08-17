from flask import Flask,request
from lang_detect import detect_lang

app = Flask(__name__)

@app.route("/")
def home():
    return "안녕~?"

@app.route("/detect")
def detect_language():
    text = request.args.get("text","")
    msg =""
    if text != "":
        lang = detect_lang(text) #text에 들어온 언어 판별
        msg = f"판정 결과 : {lang}"
    return """
    <html>
    <body>
        <form>
            <textarea name = "text" rows="8" cols="40">{0}</textarea>
            <p><input type="submit" value = "판정"></p>
            <p>{1}</p>
        </form>
    </body>
    </html>
    """.format(text, msg)

if __name__ == '__main__':
    app.run(debug=True)