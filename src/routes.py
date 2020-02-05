from flask import request
# from flask_sqlalchemy import IntegrityError
from validate_email import validate_email
from flask import current_app as app
from . import db
from .models import Request, RequestSchema
from .utils import check_book_exists, api_response


request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)


@app.route('/request', methods=['POST'])
def add_request():
    """
    Create a new Request for a book and adds it to the database.
    Requires that email is in valid format and
    title exists in the Books table.

    """

    try:
        title = request.json['title']
        email = request.json['email']

        # Validate email format
        if not validate_email(email):
            return api_response("fail", {"email": "Email provided is not in a valid format."}), 400

        # Verifiy title exists in Books table
        if not check_book_exists(title):
            return api_response("fail", {"title": f"Book {title} not found in Library"}), 404

        new_request = Request(title=title, email=email)

        db.session.add(new_request)
        db.session.commit()

        result = request_schema.dump(new_request)

        return api_response("success", result), 201

    # except IntegrityError as e:
    #     # db.session.rollback()
    #     return jsonify({"status": "error", "message": str(e)}), 400

    except Exception as e:
        # Log Error
        print(str(e))
        # db.session.rollback()
        return api_response("error", "Internal server error."), 500


@app.route('/request', methods=['GET'])
def get_all_requests():
    """ Fetch all requests """

    try:
        all_requests = Request.query.all()
        result = requests_schema.dump(all_requests)

        if not result:
            return api_response("success", "No Requests were returned."), 204

        return api_response("success", result), 200

    except Exception:
        return api_response("error", "Internal server error."), 500


@app.route('/request/<id>', methods=['GET'])
def get_request(id):
    """ Fetch one request by ID """

    try:
        request = Request.query.get(id)

        if not request:
            return api_response("error", f"Title with ID: {id} not found"), 404

        return api_response("success", request_schema.dump(request))

    except Exception:
        return api_response("error", "Internal server error."), 500


@app.route('/request/<id>', methods=['DELETE'])
def delete_request(id):
    """ Delete request by ID """

    request = Request.query.get(id)
    db.session.delete(request)
    db.session.commit()

    return api_response("success", ""), 200
