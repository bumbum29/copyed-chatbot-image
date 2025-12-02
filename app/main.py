# main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "챗봇 모델 테스트 서버 잘 동작함!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

