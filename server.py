from flask import Flask, jsonify, request, send_from_directory
import json
import os

app = Flask(__name__)

# главная страница
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# получить товары
@app.route("/products")
def products():
    if not os.path.exists("products.json"):
        return jsonify([])
    with open("products.json", "r", encoding="utf-8") as f:
        return jsonify(json.load(f))

# добавить товар (сюда шлет бот)
@app.route("/add", methods=["POST"])
def add():
    data = request.json

    if not os.path.exists("products.json"):
        products = []
    else:
        with open("products.json", "r", encoding="utf-8") as f:
            products = json.load(f)

    products.append(data)

    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    return {"status": "ok"}

# запуск
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)