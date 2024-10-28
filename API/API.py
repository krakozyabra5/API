from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def hello_world():
    data = {
      1: "Hello World!"
      }
    return jsonify(data)


@app.route('/users/', methods=['GET'])
def users():
    users = {
    1: {
        "name": "Andrey",
        "age": 19
        },
    2: {
        "name": "Raul",
        "age": 41
        },
    3: {
        "name": "Zandr",
        "age": 16
        },
    } 
    id = int(request.args.get("id"))
    return jsonify(users[id])



if __name__=="__main__":
    app.run(debug=True)

