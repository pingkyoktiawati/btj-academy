from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/about')
def about():
    return 'Docker is one of the subjects at BTJ Academy'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5070)