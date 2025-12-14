from flask import Flask, jsonify, request, abort
import time

from connect_connector import SessionMaker, Base, engine
from data_model import Package

# Initialize Flask app
app = Flask(__name__)

# Create tables if they don't exist
@app.before_request
def create_tables():
    Base.metadata.create_all(engine)

class PackageService:
    def get_package_by_product_id(self, product_id):
        session = SessionMaker()
        try:
            package = session.query(Package).filter(Package.product_id == str(product_id)).first()
            if package:
                return {
                    "height": package.height,
                    "width": package.width,
                    "depth": package.depth,
                    "weight": package.weight,
                    "special_handling_instructions": package.special_handling_instructions
                }
            return None
        finally:
            session.close()

    def create_package(self, product_id, height, width, depth, weight, special_handling_instructions):
        session = SessionMaker()
        try:
            new_package = Package(
                product_id=product_id,
                height=height,
                width=width,
                depth=depth,
                weight=weight,
                special_handling_instructions=special_handling_instructions
            )
            session.add(new_package)
            session.commit()
            return new_package.id
        finally:
            session.close()

    def update_package(self, package_id, data):
        session = SessionMaker()
        try:
            package = session.query(Package).filter(Package.id == package_id).first()
            if package:
                package.height = data.get('height', package.height)
                package.width = data.get('width', package.width)
                package.depth = data.get('depth', package.depth)
                package.weight = data.get('weight', package.weight)
                package.special_handling_instructions = data.get('special_handling_instructions', package.special_handling_instructions)
                
                session.commit()
                
                return {
                    "height": package.height,
                    "width": package.width,
                    "depth": package.depth,
                    "weight": package.weight,
                    "special_handling_instructions": package.special_handling_instructions
                }
            return None
        finally:
            session.close()

    def delete_package(self, package_id):
        session = SessionMaker()
        try:
            package = session.query(Package).filter(Package.id == package_id).first()
            if package:
                session.delete(package)
                session.commit()
                return True
            return False
        finally:
            session.close()

package_service = PackageService()

@app.route('/discovery', methods=['GET'])
def discovery():
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

@app.route('/liveness', methods=['GET'])
def liveness():
    return jsonify({
        "status": "live",
        "code": 200,
        "timestamp": time.time()
    })

@app.route('/readiness', methods=['GET'])
def readiness():
    return jsonify({
        "status": "ready",
        "code": 200,
        "timestamp": time.time()
    })

@app.route('/packages', methods=['POST'])
def create_package():
    data = request.get_json()
    product_id = data.get('product_id')
    height = data.get('height')
    width = data.get('width')
    depth = data.get('depth')
    weight = data.get('weight')
    special_handling_instructions = data.get('special_handling_instructions')

    if not all([product_id, height, width, depth, weight]):
        abort(400, description="Missing required package fields")

    package_id = package_service.create_package(product_id, height, width, depth, weight, special_handling_instructions)
    return jsonify({"package_id": package_id}), 201

@app.route('/packages/<int:product_id>', methods=['GET'])
def get_package(product_id):
    package_details = package_service.get_package_by_product_id(product_id)
    if package_details:
        return jsonify(package_details)
    abort(404, description=f"Package with product_id {product_id} not found")

@app.route('/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    data = request.get_json()
    updated_package = package_service.update_package(package_id, data)
    if updated_package:
        return jsonify(updated_package)
    abort(404, description=f"Package with package_id {package_id} not found")

@app.route('/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    if package_service.delete_package(package_id):
        return "", 204
    abort(404, description=f"Package with package_id {package_id} not found")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
