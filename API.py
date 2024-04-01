from flask import Flask, request, jsonify
from voiceAssistant import voiceAssistantOutput

app = Flask(__name__)

@app.route('/pos', methods=['POST'])
def pos():
    data = request.get_json()
    print(data)
    name , command = voiceAssistantOutput(data.get('body'))
    response = jsonify({'name': name, 'command': command})
    return response

if __name__ == '__main__':
    app.run(debug=True)

