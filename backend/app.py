from flask import Flask, request
import movie_maker

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    input = request.json['input']
    #The input will be a script written by gpt 3.5
    output = movie_maker.run(input)
    print(output)
    return {'output': output}

if __name__ == "__main__":
    pass