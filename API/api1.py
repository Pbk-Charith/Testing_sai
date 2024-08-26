from flask import Flask, jsonify

app1 = Flask(__name__)

@app1.route('/api/greet', methods=['GET'])
def greet():
    response = {
        'message': 'Hello, welcome to our API!'
    }
    return jsonify(response)

if __name__ == '__main__':
    app1.run(debug=True,port=5001)
