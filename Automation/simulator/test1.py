import json
from pathlib import Path
from flask import Flask, jsonify, request
app = Flask(__name__)
 
project_root = Path(__file__).resolve().parents[2]
config_file = project_root/"config"/"equipment.json"
 
with open(config_file, "r") as f:
    config = json.load(f)
 
for equipment_id, equipment_data in config.items():
    print(f"Equipment ID: {equipment_data['id']}")
    print(f"Name: {equipment_data['name']}")
    print(f"Type: {equipment_data['type']}")
    print(f"Status: {equipment_data['status']}")
    print("---")
 
@app.get("/api/equipment")
def get_equipment():
    return jsonify(list(config.values())), 200
 
@app.get("/api/equipment/<int:equipment_id>")
def get_equipment_by_id(equipment_id):
    return jsonify(config[str(equipment_id)]), 200
 
if __name__ == "__main__":
    app.run(debug=False, port=5000)