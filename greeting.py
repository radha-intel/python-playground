from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/<user>', methods=['POST'])
def greet(user):
    if request.method == 'POST':
        return redirect(url_for('user', usr = user))
    return f"<h1>Good Morning!!</h1>"

@app.route('/<usr>')
def user(usr):
    return f"<h1>Good Morning {usr}!!</h1>"

if __name__ == "__main__":
    app.run(debug=True)