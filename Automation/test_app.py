import pytest

from simulator.app import app


def test_get_equipment_returns_list():
    response = app.test_client().get("/api/equipment")

    assert response.status_code == 200
    data = response.get_json()
    assert [item["id"] for item in data] == [101, 102]
    assert all(item["STATUS"] == "operational" for item in data)


@pytest.mark.parametrize(
    "equipment_id",
    [
        pytest.param(101, id="equipment-101"),
        pytest.param(102, id="equipment-102"),
    ],
)
def test_equipment_page_displays_selected_id(equipment_id):
    response = app.test_client().get(f"/?id={equipment_id}")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert f"Equipment {equipment_id}" in page
    assert "flight control unit" in page


@pytest.mark.parametrize(
    ("equipment_id", "expected_data"),
    [
        pytest.param(
            101,
            {
                "id": 101,
                "name": "flight control unit",
                "type": "bFCU",
                "STATUS": "operational",
            },
            id="equipment-101",
        ),
        pytest.param(
            102,
            {
                "id": 102,
                "name": "flight control unit",
                "type": "bFCU",
                "STATUS": "operational",
            },
            id="equipment-102",
        ),
    ],
)
def test_get_equipment_by_id_returns_data(equipment_id, expected_data):
    response = app.test_client().get(f"/equipment/{equipment_id}")

    assert response.status_code == 200
    assert response.get_json() == expected_data


def test_get_missing_equipment_returns_404():
    response = app.test_client().get("/equipment/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Equipment not found"}
