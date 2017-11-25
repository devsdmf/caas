
from flask import Flask, json

# initializing flask framework
app = Flask(__name__)

# setting up after_request middleware
@app.after_request
def apply_default_headers(res):
    res.headers['Content-Type'] = 'application/json'
    res.headers['Server'] = 'CaaS.Server'
    return res

# added default entrypoint
@app.route('/')
def index():
    return json.jsonify({"hello": "caas"})

# health check endpoint
@app.route('/health',methods=['GET'])
def health_check():
    return ''

# app run
if __name__ == '__main__':
    app.run(debug=True)
