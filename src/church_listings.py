```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/prayforus'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Church(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    photos = db.Column(db.String(500))
    contact_info = db.Column(db.String(100))
    ratings = db.Column(db.Float)
    tags = db.Column(db.String(200))

    def __init__(self, name, address, photos, contact_info, ratings, tags):
        self.name = name
        self.address = address
        self.photos = photos
        self.contact_info = contact_info
        self.ratings = ratings
        self.tags = tags

class ChurchSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'photos', 'contact_info', 'ratings', 'tags')

church_schema = ChurchSchema()
churches_schema = ChurchSchema(many=True)

@app.route('/church', methods=['POST'])
def add_church():
    name = request.json['name']
    address = request.json['address']
    photos = request.json['photos']
    contact_info = request.json['contact_info']
    ratings = request.json['ratings']
    tags = request.json['tags']

    new_church = Church(name, address, photos, contact_info, ratings, tags)

    db.session.add(new_church)
    db.session.commit()

    return church_schema.jsonify(new_church)

@app.route('/church', methods=['GET'])
def get_churches():
    all_churches = Church.query.all()
    result = churches_schema.dump(all_churches)
    return jsonify(result)

@app.route('/church/<id>', methods=['GET'])
def get_church(id):
    church = Church.query.get(id)
    return church_schema.jsonify(church)

if __name__ == '__main__':
    app.run(debug=True)
```