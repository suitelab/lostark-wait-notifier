# -*- coding: utf-8 -*-

# ---------------------------------
# pangpang2.py
# ---------------------------------

import os
from flask import Flask, request, jsonify
from Crawler import *
import json

app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type": "buttons",
        "buttons": ["대기열", "도움말"]
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"대기열":
        # cr = Crawler()
        # json_file = cr.start("http://loaq.kr/")
        json_file = json.load(open('test.json', "r", encoding="utf-8"))

        dataSend = {
            "message": {
                "text": json_file["server_time"] + "\n루페온 : 1000\n크로나 : 2000"
            }
        }
    elif content == u"명령어":
        dataSend = {
            "message": {
                "text": "1. 대기열\n2. 명령어"
            }
        }
    else:
        dataSend = {
            "message": {
                "text": "명령어를 다시 입력해주세요. 1. 대기열, 2.명령어"
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=8080)