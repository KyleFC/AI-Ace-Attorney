from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import movie_maker

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    if not request.is_json:
        return jsonify({"error": "Request does not have a JSON body"}, 400)
    
    if 'input' not in request.json:
        return jsonify({"error": "JSON body does not include 'input' key"}, 400)
    
    topic = request.json['input']
    movie_maker.movie_maker(topic)
    return jsonify({'message': 'Video created successfully'}), 200

@app.route('/video', methods=['GET'])
def get_video():
    return send_file('output.mp4', mimetype='video/mp4')





if __name__ == "__main__":
    app.run(debug=False)