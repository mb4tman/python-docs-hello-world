from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PoC - Domain Takeover. ~ by:b4tman"
