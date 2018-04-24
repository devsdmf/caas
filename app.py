
from correios import Correios
from correios.package import *
from flask import Flask, request, json

# initializing flask framework
app = Flask(__name__)

# setting up before_request middlewares

# setting up after_request middlewares
@app.after_request
def apply_default_headers(res):
    res.headers['Content-Type'] = 'application/json'
    res.headers['Server'] = 'CaaS.Server'
    return res

# setting up default routes
# @app.route('/')
# def index():
#     return json.jsonify({"hello": "caas"})

@app.errorhandler(400)
def bad_request(error):
    return make_response(
        json.jsonify({"success": False, "error": "Invalid request, please check out the API documentation"}),
        400
    )

@app.errorhandler(404)
def not_found(error):
    return make_response(json.jsonify({"success": False, "error": "The requested resource was not found"}),404)

# health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return ''

@app.route('/shipping/rate', methods=['POST'])
def create_shipping_rate():
    if not request.is_json():
        abort(400)
    
    req = request.get_json()
    requestedPackage = req['package']

    if (requestedPackage['type'] == 'box'):
        package = BoxPackage()
        package.add_item(
            requestedPackage['height'],
            requestedPackage['width'],
            requestedPackage['depth'],
            requestedPackage['weight']
        )
    elif (requestedPackage['type'] == 'cylinder'):
        package = CylinderPackage()
        package.add_item(requestedPackage['length'],requestedPackage['diameter'],requestedPackage['weight'])
    elif (requestedPackage['type'] == 'envelope'):
        package = EnvelopePackage()
        package.add_item(requestedPackage['width'],requestedPackage['lenght'],requestedPackage['weight'])
    else:
        abort(400)
    
    

# app run
if __name__ == '__main__':
    app.run(debug=True)
