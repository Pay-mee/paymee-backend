from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


usuarios = [
    {"login": "Steicy",
     "password": "1234",
     "role": "manager"},
    {"login": "Gabriel",
     "password": "1234",
     "role": "user"},
    {"login": "Lucas",
     "password": "1234",
     "role": "contability"},
    {"login": "William",
     "password": "1234",
     "role": "user"}
]

@app.route("/")
def home():
    return "Pay-mee"

@app.route("/login", methods = ["POST"])
@cross_origin()
def login():
    data = request.get_json()
    login = data["login"]
    password = data["password"]
    for usuario in usuarios:
        if usuario["login"] == login:
            if usuario["password"] == password:
                return {"Message": "Success!", "role": usuario["role"]}
    return {"Message": "Not exist!"}


if __name__ == "__main__":
    app.run(debug=True)