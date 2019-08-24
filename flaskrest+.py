from flask import Flask, request
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/language','lang')

class Language(Resource):
    def get(self):
        return {"Color": "Yellow", "Area":"North","K":"6"}, 200

    def post(self):
        dict1 = request.json
        return dict1, 200

if __name__ == "__main__":
    app.run(debug=True)