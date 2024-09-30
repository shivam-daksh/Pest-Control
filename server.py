from flask import Flask

# setup flask server
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001, debug=True)