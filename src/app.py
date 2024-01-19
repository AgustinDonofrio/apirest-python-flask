from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

### Prueba de ping al servidor
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Conectado!"})

@app.route('/products', methods=['GET'])
def gerProducts():
    return jsonify({"products": products})

@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    product_found = [product for product in products if product["name"] == product_name]

    if product_found:
        return jsonify({"product": product_found[0]})
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price":request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    print(products)
    return jsonify({"message": "Product added succesfully"})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    product_found = [product for product in products if product['name'] == product_name]

    if product_found:
        product_found[0]['name'] = request.json['name']
        product_found[0]['price'] = request.json['price']
        product_found[0]['quantity'] = request.json['quantity']
        return jsonify({"message": "Product updated succesfully"})
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    product_found = [product for product in products if product['name'] == product_name]

    if product_found:
        products.remove(product_found[0])
        return jsonify({"message": "Product deleted succesfully"})
    else:
        return jsonify({"message": "Product not found"}), 404

if (__name__ == '__main__'):
    app.run(debug=True, port=3000)