# flask_web/app.py

from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.secret_key = 'my_key'
app.debug = True

username = ""

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/expenses')
def expenses():
    return render_template('expenses.html', username=username)

@app.route("/setname", methods=["POST"])
def setname():
    global username
    username = request.form["username"]
    return redirect('/expenses')
    return expenses()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

