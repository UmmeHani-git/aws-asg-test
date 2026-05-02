from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cart = []

@app.route('/')
def home():
    return "Backend Healthy!"

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.json
    item = data.get('item')

    cart.append(item)

    return jsonify({
        "status": "success",
        "message": f"{item} added to cart!"
    })

@app.route('/cart')
def get_cart():
    return jsonify(cart)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
