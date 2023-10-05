```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# User Class/Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    bank_account = db.Column(db.String(200))

    def __init__(self, first_name, last_name, email, password, bank_account):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.bank_account = bank_account

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'bank_account')

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create a User
@app.route('/user', methods=['POST'])
def add_user():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    bank_account = request.json['bank_account']

    new_user = User(first_name, last_name, email, password, bank_account)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
```