# flask_web/app.py

from flask import Flask, render_template, redirect, request, jsonify
import csv
import json
import os

app = Flask(__name__)
# app.secret_key = 'my_key'
app.debug = True

username = ""

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/expenses')
def expenses():
    with open(os.path.join(os.path.dirname(__file__),'./templates/static/csv/expenses.csv')) as csv_file:
        #first_line = True
        # Name,Connected Accounts,Category,Earned,Expenses,Savings Goal,Total Income
        expenses = []
        data= csv.DictReader(csv_file)
        for row in data:
            expenses.append(row)

   #  expenses_json = jsonify({'result': expenses})
    return render_template('expenses.html', username=username)

@app.route("/setname", methods=["POST"])
def setname():
    global username
    username = request.form["username"]
    return redirect('expenses')
    return expenses()

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
