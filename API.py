from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pos', methods=['POST'])

