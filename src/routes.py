from flask import request, jsonify
# from flask.ext.api.exceptions import APIException, NotFound
from flask import current_app as app
from .models import Request, RequestSchema, db


request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)


@app.route('/request', methods=['POST'])
def add_request():
    """
    Create a new Request for a book and add to the database
    """

    # TODO: Validate request: email is valid format, title is in database

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

    if not result:
        result = {'result': 'No Requests were returned.'}

    return jsonify(result)


@app.route('/request/<id>', methods=['GET'])
def get_request(id):
    """ Fetch one request by ID """

    try:
        request = Request.query.get(id)

        if not request:
            raise ValueError(f'Request for id: {id} not found.')

        return request_schema.jsonify(request)

    except ValueError as e:
        return {"error": str(e)}, 404


@app.route('/request/<id>', methods=['DELETE'])
def delete_request(id):
    """ Delete request by ID """

    request = Request.query.get(id)
    db.session.delete(request)
    db.session.commit()

    return request_schema.jsonify(request)
