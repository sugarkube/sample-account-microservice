from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {'name': 'Example user'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
