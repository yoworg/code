from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/test", methods = ["GET", "POST"])
def hello():
    request_body = request.get_json()
    return {"Hi":request_body}


if __name__ == "__main__":
    app.run(debug=True)