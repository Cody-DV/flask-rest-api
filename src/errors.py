from flask import jsonify
from flask import current_app as app


class BadRequest(Exception):
    """
    Custom exception class to be thrown when local error occurs.

    Params:
        data: dict message indicating the violating parameter.
            Ex. {"example_param": "Invalid example parameter"}

    """

    def __init__(self, data):
        self.data = data


class NotFound(Exception):
    """
    Custom exception class to be thrown when local error occurs.

    Params:
        data: string message indicating the missing resource
    """

    def __init__(self, data):
        self.data = data


@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """
    Catch BadRequest exception globally,
    serialize into JSON, and respond with 400.
    """
    payload = dict()
    payload['status'] = 'fail'
    payload['data'] = error.data
    return jsonify(payload), 400


@app.errorhandler(NotFound)
def handle_not_found(error):
    """
    Catch NotFound exception globally,
    serialize into JSON, and respond with 404.
    """
    payload = dict()
    payload['status'] = 'error'
    payload['message'] = error.data
    return jsonify(payload), 404


@app.errorhandler(Exception)
def handle_uncaught_exception(error):
    """
    Catch Exception globally,
    serialize into JSON, and respond with 500.
    """
    payload = dict()
    payload['status'] = 'error'
    payload['message'] = "Internal Server Error"
    return jsonify(payload), 500
