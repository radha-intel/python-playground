from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello():
    return render_template("hello.html")

if __name__ == "__main__":
    app.run()
    