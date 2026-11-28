import json
from pathlib import Path
from flask import Flask, jsonify

app = Flask(__name__)

config_file = Path(__file__).resolve().parents[2] / "config" / "config.json"
with config_file.open(encoding="utf-8") as config_file_handle:
    equipment_data = json.load(config_file_handle)

config = {str(item["id"]): item for item in equipment_data}

for equipment_id, equipment_data in config.items():
    print(f"Equipment ID: {equipment_data['id']}")
    print(f"Name: {equipment_data['name']}")
    print(f"Type: {equipment_data['type']}")
    print(f"Status: {equipment_data['STATUS']}")
    print("---")


@app.get("/api/equipment")
def get_equipment():
    return jsonify(list(config.values())), 200


@app.get("/api/equipment/<int:equipment_id>")
def get_equipment_by_id(equipment_id):
    item = config.get(str(equipment_id))
    if item is None:
        return jsonify({"error": "Equipment not found"}), 404
    return jsonify(item), 200


if __name__ == "__main__":
    app.run(debug=False, port=5000)