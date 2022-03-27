import os
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, static_url_path='/static')
@app.route("/")
def open_html():
    return render_template('sad.html')
#<link rel="stylesheet"; type="text/html"; href="/static/sad.html">

@app.route('/list', methods=['GET'])
def query_records():
    #name = request.args.get('name')
    with open('file.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        #for record in records:
        return jsonify(records)

@app.route('/list_', methods=['POST'])
def update_record():
    if request.method == "POST":
        newItem = request.form.get("nm")
        #print(jsonify(newItem_))
        return jsonify(newItem)
    #return render_template("sad.html")

if __name__ == '__main__':
    app.run()