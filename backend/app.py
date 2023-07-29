from flask import Flask, request
from flask_cors import CORS
import movie_maker

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    if not request.is_json:
        return {"error": "Request does not have a JSON body"}, 400
    if 'input' not in request.json:
        return {"error": "JSON body does not include 'input' key"}, 400
    script = request.json['input']
    output = movie_maker.movie_maker(script)
    print(output)
    return {'output': output}






if __name__ == "__main__":
    app.run(debug=True)