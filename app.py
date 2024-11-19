from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)     # initialize the database

# Creates the database cols
class Todo(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     content = db.Column(db.String(200), nullable = False)
     completed = db.Column(db.Integer,default = 0)
     date_created = db.Column(db.DateTime,default = datetime.now)

#? We run a flask shell and then use 'from app import db' to initialize the object. If nothing is returned then the object is poinnting to the correct database and everything is working fine

# Returns a string everytime a new element is created
     def __repr__(self):
          return '<Task %r>' % self.id


@app.route('/', methods =['POST','GET'])
def index():
     return render_template('index.html')

if __name__ == "__main__":
     app.run(debug=True)