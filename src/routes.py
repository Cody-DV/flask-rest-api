from flask import request
from validate_email import validate_email
from flask import current_app as app
from . import db
from .models import Request, RequestSchema
from .utils import check_book_exists, api_response
from .errors import BadRequest, NotFound


request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)


@app.route('/', methods=['GET'])
def welcome():
    return api_response("Welcome - Server is live"), 200


@app.route('/request', methods=['POST'])
def add_request():
    """
    Create a new Request for a book and adds it to the database.
    Requires that email is in valid format and
    title exists in the Books table.

    """

    title = request.json['title']
    email = request.json['email']

    # Validate email format
    if not validate_email(email):
        raise BadRequest({"email": "Email provided is not in a valid format."})

    # Verify title exists in Books table
    if not check_book_exists(title):
        raise BadRequest({"title": f"Book {title} not found in Library"})

    new_request = Request(title=title, email=email)

    db.session.add(new_request)
    db.session.commit()

    result = request_schema.dump(new_request)

    return api_response(result), 201


@app.route('/request', methods=['GET'])
def get_all_requests():
    """ Fetch all requests """

    all_requests = Request.query.all()
    result = requests_schema.dump(all_requests)

    if not result:
        return api_response("No Requests were returned"), 204

    return api_response(result), 200


@app.route('/request/<id>', methods=['GET'])
def get_request(id):
    """ Fetch one request by ID """

    request = Request.query.get(id)

    if not request:
        raise NotFound(f"Title with ID: {id} not found")

    return api_response(request_schema.dump(request)), 200


@app.route('/request/<id>', methods=['DELETE'])
def delete_request(id):
    """ Delete request by ID """

    request = Request.query.get(id)
    if not request:
        raise NotFound(f"Request with ID: {id} not found")
    db.session.delete(request)
    db.session.commit()

    return api_response(), 200
