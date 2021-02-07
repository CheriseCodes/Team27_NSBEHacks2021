import csv
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.secret_key = 'my_key'
app.debug = True

username = ""

@app.route('/')
def home():
    return render_template('home.html')



@app.route("/expenses")
def expenses():
  with open('nsbe_hacks_2021.csv') as csv_file:
    data = csv.reader(csv_file, delimiter='|')
    first_line = True
    expenses = []
    for row in data:
      if not first_line:
        expenses.append({
          "Name": row[0],
          "connected acoounts": row[1],
          "upcoming bills": row[2],
          "Earned": row[3],
          "Expenses": row[4],
          "Savings Goal": row[5],
          "Total Income": row[6]
        })
      else:
        first_line = False
  return render_template("expenses.html", expenses=expenses)

@app.route("/setname", methods=["POST"])
def setname():
    global username
    username = request.form["username"]
    return redirect('/expenses')
    return expenses()

@app.route("/setname", methods=["POST"])
def setname():
    global username
    username = request.form["username"]
    return redirect('/expenses')
    return expenses()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





data_list = [["Name", "connected accounts", "upcoming bills", "Earned", "Expenses", "Savings Goal", "Total Income"],
        ["John", "Chase", "TV Streaming", "500.00", "200.00", "900.00", "999.99"],
         ["Bob", "TD", "rent", "1,450.00", "800.00", "20,000.00", "50,000.00"],
         ["Jason", "Bank of America", "Pacific Gas and Electric", "4,000.00", "1,200.00", "24,000.00", "60,000.00"],
         ["Ashley", "M&T Bank", "Cell Phone", "3,000.00", "200.00", "9,000.00", "20,000.00"],
         ["Mohamad", "KeyBank", "rent", "1,450.00", "800.00", "20,000.00", "50,000.00"],
         ["Stephen", "PNC Bank", "Car Load", "2,000.00", "450.00", "10,000.00", "50,000.00"],
                 ["James", "Chase", "TV Streaming", "500.00", "200.00", "900.00", "999.99"],
         ["Molly", "TD", "rent", "1,450.00", "800.00", "20,000.00", "50,000.00"],
         ["Kevin", "Bank of America", "Pacific Gas and Electric", "4,000.00", "1,200.00", "24,000.00", "60,000.00"],
         ["Karen", "M&T Bank", "Cell Phone", "3,000.00", "200.00", "9,000.00", "20,000.00"],
         ["Jeff", "KeyBank", "rent", "1,450.00", "800.00", "20,000.00", "50,000.00"],
         ["Stephne", "PNC Bank", "Car Load", "2,000.00", "450.00", "10,000.00", "50,000.00"]]



with open('nsbe_hacks_2021.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_list)

