from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "안녕하세요! 제 첫 웹사이트입니다."

if __name__ == "__main__":
    app.run()
