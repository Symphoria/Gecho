import sys
import os
from datetime import datetime
from test_image import get_result
from flask import Flask

app = Flask(__name__)

@app.route("/testImage", methods = ["GET"])
def test_image():
    result = get_result()
    if result == 'time':
        current_time = datetime.now()
        formatted_time = current_time.strftime("%d %B %A %I %M %p")
        return formatted_time

    return result


app.run(port=8000, debug=True)
