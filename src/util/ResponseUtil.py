from flask import jsonify
import json
class ResponseUtil:

    def build_error_response(self, code, message):
        response = jsonify(
            {
                'status' : 'error',
                'code' : code,
                'message' : message
            }
        )
        response.status_code = code
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    def build_success_response(self, code, message, data):
        if type(data) is dict:
            parsed = data
        elif type(data) is str:
            parsed = json.loads(data)

        response = jsonify(
            {
                'status' : 'ok',
                'code' : code,
                'message': message,
                'result' : parsed,
            }
        )
        response.status_code = code
        response.headers['Access-Control-Allow-Origin'] = '*'


        return response