from flask import Flask, render_template
# pip install flask 설치 명령어
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, DevOps!"

#route menu 추가
@app.route("/meun")
def meun():
    return render_template("menu.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)