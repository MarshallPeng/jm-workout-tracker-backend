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
        return response

    def build_success_response(self, code, message, data):
        parsed = json.loads(data)

        response = jsonify(
            {
                'status' : 'ok',
                'code' : code,
                'message': message,
                'result' : parsed
            }
        )


        return response