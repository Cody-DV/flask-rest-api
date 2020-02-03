from flask import Flask, request, jsonify
# from flask.ext.api.exceptions import APIException, NotFound
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init App
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# TODO: Move db to docker container

# Init DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Init ma - look into alternatives
ma = Marshmallow(app)


# Move to models.py
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    email = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=db.func.now())

    def __repr__(self):
        return(f'<Title: {self.title} Email: {self.email}')


# Define Schema
class RequestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'email', 'timestamp')


request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)


@app.route('/request', methods=['POST'])
def add_request():
    """
    Create a new Request for a book and add to the database
    """

    title = request.json['title']
    email = request.json['email']

    new_request = Request(title=title, email=email)

    db.session.add(new_request)
    db.session.commit()

    return request_schema.jsonify(new_request)


@app.route('/request', methods=['GET'])
def get_all_requests():
    """ Fetch all requests """

    all_requests = Request.query.all()
    result = requests_schema.dump(all_requests)

    return jsonify(result)


@app.route('/request/<id>', methods=['GET'])
def get_request(id):
    """ Fetch one request by ID """

    try:
        request = Request.query.get(id)

        if not request:
            raise RuntimeError(f'Request for id: {id} not found.')

        return request_schema.jsonify(request)

    except RuntimeError as e:
        return {"error": str(e)}, 404


@app.route('/request/<id>', methods=['DELETE'])
def delete_request(id):
    """ Delete request by ID """

    request = Request.query.get(id)
    db.session.delete(request)
    db.session.commit()

    return request_schema.jsonify(request)


if __name__ == "__main__":
    app.run(debug=True)
