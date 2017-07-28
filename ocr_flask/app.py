# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 01:02:02 2016

@author: abhishek
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from werkzeug.utils import secure_filename
from ocr import process_image

app = Flask(__name__)
_VERSION = 1  # API version

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/v{}/ocr'.format(_VERSION), methods=["POST"])
def ocr():
    try:
        url = request.json['image_url']
#        if 'jpg' in url:
        output = process_image(url)
        return jsonify({"output": output})
#        else:
#            return jsonify({"error": "only .jpg files, please"})
    except:
        return jsonify(
            {"error": "Did you mean to send: {'image_url': 'some_jpeg_url'}"}
        )


@app.errorhandler(500)
def internal_error(error):
    print str(error)  # ghetto logging


@app.errorhandler(404)
def not_found_error(error):
    print str(error)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)

    

