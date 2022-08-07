from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key ="hello"

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
 
db = SQLAlchemy(app)
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(1000))
    phone = db.Column(db.String(1000))
    order = db.Column(db.String(1000))
    price = db.Column(db.String(1000))

    def __init__(self, name, email, phone, order, price):
        self.name = name
        self.email = email
        self.phone = phone
        self.order = order
        self.price = price


@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        order = request.form['order']
        price = request.form['price']

        my_data = Data(name, email, phone, order, price)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug = True)