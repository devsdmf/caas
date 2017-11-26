
from flask import Flask, json

# initializing flask framework
app = Flask(__name__)

# setting up after_request middleware
@app.after_request
def apply_default_headers(res):
    res.headers['Content-Type'] = 'application/json'
    res.headers['Server'] = 'CaaS.Server'
    return res

# setting up default routes
@app.route('/')
def index():
    return json.jsonify({"hello": "caas"})

@app.errorhandler(404)
def not_found(error):
    return make_response(json.jsonify({"error": "Resource not found"}),404)

# health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return ''

@app.route('/shipping/rate', methods=['POST'])
def create_shipping_rate():
    pass

# app run
if __name__ == '__main__':
    app.run(debug=True)
