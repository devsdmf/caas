
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, CaaS!"

@app.route('/health',methods=['GET'])
def health_check():
    return ''

if __name__ == '__main__':
    app.run(debug=True)
