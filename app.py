from flask import Flask

app = Flask(__name__)

@app.route("/taxis")
def taxis():
    return "Hello, World!"