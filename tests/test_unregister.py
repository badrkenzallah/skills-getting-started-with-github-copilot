from fastapi.testclient import TestClient
from src.app import app, activities

client = TestClient(app)


def test_unregister_success():
    # Add a temp participant
    activity = "Basketball"
    email = "temp-test@mergington.edu"
    if email not in activities[activity]["participants"]:
        activities[activity]["participants"].append(email)

    response = client.delete(f"/activities/{activity}/participants?email={email}")
    assert response.status_code == 200
    assert email not in activities[activity]["participants"]


def test_unregister_not_found():
    response = client.delete("/activities/Basketball/participants?email=noone@nowhere.edu")
    assert response.status_code == 404
