from flask import Flask, jsonify
import os

app = Flask(__name__)

products = [
    {"name": "Brawl Stars", "desc": "35к кубков", "price": 499},
    {"name": "Clash Royale", "desc": "14 уровень", "price": 699},
    {"name": "Clash of Clans", "desc": "TH15", "price": 999}
]

@app.route("/")
def home():
    return "OK"

@app.route("/products")
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))