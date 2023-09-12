from flask import Flask, request

app = Flask(__name__)

usuarios = [
    {"login": "Steicy",
     "password": "1234",
     "role": "admin"},
    {"login": "Gabriel",
     "password": "1234",
     "role": "admin"},
    {"login": "Lucas",
     "password": "1234",
     "role": "user"},
    {"login": "William",
     "password": "1234",
     "role": "user"}
]

@app.route("/")
def home():
    return "Hello, World! editado"

@app.route("/login", methods = ["POST"])
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