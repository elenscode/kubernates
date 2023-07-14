from flask import Flask, request
from flasgger import Swagger
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


class Username(Resource):
    def get(self, username):
        """
        This examples uses FlaskRESTful Resource
        It works also with swag_from, schemas and spec_dict
        ---
        parameters:
          - in: path
            name: username
            type: string
            required: true
        responses:
          200:
            description: A single user item
            schema:
              id: User
              properties:
                username:
                  type: string
                  description: The name of the user
                  default: Steven Wilson
        """
        return {"username": username}, 200

    def post(self, username):
        """
        This examples uses FlaskRESTful Resource
        It works also with swag_from, schemas and spec_dict
        ---
        responses:
          200:
            description: A single user item
            schema:
              id: User
              properties:
                username:
                  type: string
                  description: The name of the user
                  default: Steven Wilson
        """

        params = request.get_json()
        return {username: params}, 200

api.add_resource(Username, "/username/<username>")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
