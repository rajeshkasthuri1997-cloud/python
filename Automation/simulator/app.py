import json
from pathlib import Path

from flask import Flask, jsonify, render_template_string, request


config_path = Path(__file__).resolve().parents[2] / "config" / "config.json"
with config_path.open(encoding="utf-8") as config_file:
    equipment_data = json.load(config_file)

app = Flask(__name__)

equipment = {item["id"]: item for item in equipment_data}

# Preserve the original misspelled name for compatibility.
equipments = equipment
equiments = equipment


@app.get("/")
def equipment_page():
    selected_id = request.args.get("id", type=int)
    selected_equipment = equipment.get(selected_id) if selected_id is not None else None

    return render_template_string(
        """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Equipment lookup</title>
  </head>
  <body>
    <h1>Equipment lookup</h1>
    <form method="get">
      <label for="equipment-id">Select equipment ID:</label>
      <select id="equipment-id" name="id" onchange="this.form.submit()">
        <option value="">Choose an ID</option>
        {% for equipment_id in equipment_ids %}
        <option value="{{ equipment_id }}" {% if equipment_id == selected_id %}selected{% endif %}>{{ equipment_id }}</option>
        {% endfor %}
      </select>
      <noscript><button type="submit">Show equipment</button></noscript>
    </form>
    {% if selected_equipment %}
    <h2>Equipment {{ selected_equipment["id"] }}</h2>
    <dl>
      {% for key, value in selected_equipment.items() %}
      <dt>{{ key }}</dt>
      <dd>{{ value }}</dd>
      {% endfor %}
    </dl>
    {% elif selected_id is not none %}
    <p>Equipment {{ selected_id }} was not found.</p>
    {% else %}
    <p>Select an ID to view its data.</p>
    {% endif %}
  </body>
</html>""",
        equipment_ids=sorted(equipment),
        selected_id=selected_id,
        selected_equipment=selected_equipment,
    )


@app.get("/api/equipments")
@app.get("/api/equipment")
@app.get("/equipment")
def get_equipment():
    return jsonify(list(equipment.values())), 200


@app.get("/api/equipments/<int:equipment_id>")
@app.get("/api/equipment/<int:equipment_id>")
@app.get("/equipment/<int:equipment_id>")
def get_equipment_by_id(equipment_id):
    item = equipment.get(equipment_id)
    if item is None:
        return jsonify({"error": "Equipment not found"}), 404
    return jsonify(item)


if __name__ == "__main__":
    # debug=True enables auto-reload on code changes and detailed error pages
    app.run(debug=True)