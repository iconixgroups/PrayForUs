```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/prayforus'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    saved_churches = db.Column(db.String(500))
    bookings = db.Column(db.String(500))
    donations = db.Column(db.String(500))
    event_registrations = db.Column(db.String(500))
    payment_methods = db.Column(db.String(500))

    def __init__(self, first_name, last_name, email, password, saved_churches, bookings, donations, event_registrations, payment_methods):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.saved_churches = saved_churches
        self.bookings = bookings
        self.donations = donations
        self.event_registrations = event_registrations
        self.payment_methods = payment_methods

class UserProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'saved_churches', 'bookings', 'donations', 'event_registrations', 'payment_methods')

user_profile_schema = UserProfileSchema()
user_profiles_schema = UserProfileSchema(many=True)

@app.route('/user_profile', methods=['POST'])
def add_user_profile():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    saved_churches = request.json['saved_churches']
    bookings = request.json['bookings']
    donations = request.json['donations']
    event_registrations = request.json['event_registrations']
    payment_methods = request.json['payment_methods']

    new_user_profile = UserProfile(first_name, last_name, email, password, saved_churches, bookings, donations, event_registrations, payment_methods)

    db.session.add(new_user_profile)
    db.session.commit()

    return user_profile_schema.jsonify(new_user_profile)

@app.route('/user_profile', methods=['GET'])
def get_user_profiles():
    all_user_profiles = UserProfile.query.all()
    result = user_profiles_schema.dump(all_user_profiles)
    return jsonify(result)

@app.route('/user_profile/<id>', methods=['GET'])
def get_user_profile(id):
    user_profile = UserProfile.query.get(id)
    return user_profile_schema.jsonify(user_profile)

@app.route('/user_profile/<id>', methods=['PUT'])
def update_user_profile(id):
    user_profile = UserProfile.query.get(id)

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    saved_churches = request.json['saved_churches']
    bookings = request.json['bookings']
    donations = request.json['donations']
    event_registrations = request.json['event_registrations']
    payment_methods = request.json['payment_methods']

    user_profile.first_name = first_name
    user_profile.last_name = last_name
    user_profile.email = email
    user_profile.password = password
    user_profile.saved_churches = saved_churches
    user_profile.bookings = bookings
    user_profile.donations = donations
    user_profile.event_registrations = event_registrations
    user_profile.payment_methods = payment_methods

    db.session.commit()

    return user_profile_schema.jsonify(user_profile)

@app.route('/user_profile/<id>', methods=['DELETE'])
def delete_user_profile(id):
    user_profile = UserProfile.query.get(id)
    db.session.delete(user_profile)
    db.session.commit()

    return user_profile_schema.jsonify(user_profile)

if __name__ == '__main__':
    app.run(debug=True)
```