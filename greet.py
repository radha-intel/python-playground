from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        user = request.json['usr']
        return f"<h1>Good Morning {user}!!</h1>"
    return f"<h1>Good Morning!!</h1>"

if __name__ == "__main__":
    app.run(debug=True)