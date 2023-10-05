```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), unique=True)
    ticket_quantity = db.Column(db.Integer)
    ticket_type = db.Column(db.String(50))

    def __init__(self, event_name, ticket_quantity, ticket_type):
        self.event_name = event_name
        self.ticket_quantity = ticket_quantity
        self.ticket_type = ticket_type

class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'event_name', 'ticket_quantity', 'ticket_type')

event_schema = EventSchema()
events_schema = EventSchema(many=True)

@app.route('/event', methods=['POST'])
def add_event():
    event_name = request.json['event_name']
    ticket_quantity = request.json['ticket_quantity']
    ticket_type = request.json['ticket_type']

    new_event = Event(event_name, ticket_quantity, ticket_type)

    db.session.add(new_event)
    db.session.commit()

    return event_schema.jsonify(new_event)

@app.route('/event', methods=['GET'])
def get_events():
    all_events = Event.query.all()
    result = events_schema.dump(all_events)
    return jsonify(result)

@app.route('/event/<id>', methods=['GET'])
def get_event(id):
    event = Event.query.get(id)
    return event_schema.jsonify(event)

@app.route('/event/<id>', methods=['PUT'])
def update_event(id):
    event = Event.query.get(id)

    event_name = request.json['event_name']
    ticket_quantity = request.json['ticket_quantity']
    ticket_type = request.json['ticket_type']

    event.event_name = event_name
    event.ticket_quantity = ticket_quantity
    event.ticket_type = ticket_type

    db.session.commit()

    return event_schema.jsonify(event)

@app.route('/event/<id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()

    return event_schema.jsonify(event)

if __name__ == '__main__':
    app.run(debug=True)
```