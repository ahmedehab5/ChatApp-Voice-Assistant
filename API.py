from flask import Flask, request, jsonify
from voiceAssistant import voiceAssistantOutput
from flask_cors import CORS

app = Flask(__name__)

@app.route('/get-command-and-name', methods=['POST'])
def pos():
    print('request : ' , request)
    print('request.json : ' , request.json)
    data = request.get_json()
    print('data :' , data)
    name , command = voiceAssistantOutput(data.get('text'))
    response = jsonify({'name': name, 'command': command})
    return response

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)
    