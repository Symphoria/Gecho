import sys
from webcam import invoke_webcam
from flask import Flask

app = Flask(__name__)

@app.route("/invoke", methods = ["GET"])
def invoke():
    invoke_webcam()
    return 'success'

app.run(port=5000, debug=True)