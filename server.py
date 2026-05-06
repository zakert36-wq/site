from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "name": "Brawl Stars аккаунт",
        "desc": "35к кубков, легендарки",
        "price": 499
    },
    {
        "name": "Clash Royale аккаунт",
        "desc": "Все карты, 14 уровень",
        "price": 699
    },
    {
        "name": "Clash of Clans аккаунт",
        "desc": "TH15, фулл база",
        "price": 999
    }
]

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/")
def home():
    return "SERVER WORKING"

app.run(host="0.0.0.0", port=3000)