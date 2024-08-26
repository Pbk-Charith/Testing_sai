from flask import Flask 

app = Flask(__name__)

@app.route('/charith')
def home():
    return "API Created"

if __name__ == '__main__':
    app.run(debug=True)

else:
    print("Flask app is being imported as a module.")