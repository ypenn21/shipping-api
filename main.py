from flask import Flask, jsonify, request, abort
import time

from db_connector import SessionMaker, Base, engine
from data_model import Package

# Initialize Flask app
app = Flask(__name__)

# Create tables if they don't exist
@app.before_request
def create_tables():
    Base.metadata.create_all(engine)



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
    package_id_val = data.get('package_id')
    height = data.get('height')
    width = data.get('width')
    depth = data.get('depth')
    weight = data.get('weight')
    special_handling_instructions = data.get('special_handling_instructions')

    if not all([package_id_val, height, width, depth, weight]):
        abort(400, description="Missing required package fields")

    session = SessionMaker()
    try:
        new_package = Package(
            package_id=package_id_val,
            height=height,
            width=width,
            depth=depth,
            weight=weight,
            special_handling_instructions=special_handling_instructions
        )
        session.add(new_package)
        session.commit()
        db_id = new_package.id
        return jsonify({"db_id": db_id, "package_id": package_id_val}), 201
    finally:
        session.close()

@app.route('/packages/<int:package_id>', methods=['GET'])
def get_package(package_id):
    session = SessionMaker()
    try:
        package = session.query(Package).filter(Package.package_id == str(package_id)).first()
        if package:
            package_details = {
                "package_id": package.package_id,
                "height": package.height,
                "width": package.width,
                "depth": package.depth,
                "weight": package.weight,
                "special_handling_instructions": package.special_handling_instructions
            }
            return jsonify(package_details)
        abort(404, description=f"Package with package_id {package_id} not found")
    finally:
        session.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
