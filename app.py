from flask import Flask, render_template
import socket
# pip install flask 설치 명령어
app = Flask(__name__)

@app.route('/')
def home():
    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '

    return render_template('index.html', computername=hostname)

#def hello_world():
#    return "Hello, DevOps!"

#route menu 추가
@app.route("/menu")
def meun():
    return render_template("menu.html")

#route test1 추가
@app.route("/test1")
def test1():
    return render_template('test1.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    print(f"__debug__ is {__debug__}")
