import sys
import os
from webcam import invoke_webcam
from test_image import get_result
from flask import Flask

app = Flask(__name__)

@app.route("/testImage", methods = ["GET"])
def test_image():
    result = get_result()

    return result


app.run(port=8000, debug=True)