from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        user = request.form['usr']
        return redirect(url_for('user', usr = user))
    return render_template("greet.html")

@app.route('/<usr>')
def user(usr):
    return f"<h1>Good Morning {usr}!!</h1>"

if __name__ == "__main__":
    app.run(debug=True)