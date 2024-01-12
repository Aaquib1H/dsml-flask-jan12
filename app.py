from flask import Flask
from joblib import load

app = Flask(__name__)

print(__name__)

clf = load('Dragon.joblib') 



@app.route("/ping", methods = ["GET"])
def ping():
    return "Pinging Model Application!!"

