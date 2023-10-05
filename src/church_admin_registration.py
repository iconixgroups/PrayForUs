```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/prayforus'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class ChurchAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    church_name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    photos = db.Column(db.String(500))
    contact_info = db.Column(db.String(100))
    service_categories = db.Column(db.String(200))
    fees = db.Column(db.String(100))

    def __init__(self, church_name, address, photos, contact_info, service_categories, fees):
        self.church_name = church_name
        self.address = address
        self.photos = photos
        self.contact_info = contact_info
        self.service_categories = service_categories
        self.fees = fees

class ChurchAdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'church_name', 'address', 'photos', 'contact_info', 'service_categories', 'fees')

admin_schema = ChurchAdminSchema()
admins_schema = ChurchAdminSchema(many=True)

@app.route('/admin', methods=['POST'])
def add_admin():
    church_name = request.json['church_name']
    address = request.json['address']
    photos = request.json['photos']
    contact_info = request.json['contact_info']
    service_categories = request.json['service_categories']
    fees = request.json['fees']

    new_admin = ChurchAdmin(church_name, address, photos, contact_info, service_categories, fees)

    db.session.add(new_admin)
    db.session.commit()

    return admin_schema.jsonify(new_admin)

@app.route('/admin', methods=['GET'])
def get_admins():
    all_admins = ChurchAdmin.query.all()
    result = admins_schema.dump(all_admins)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
```