from fastapi.testclient import TestClient
from src.app import app, activities

client = TestClient(app)


def test_signup_updates_activity():
    activity = "Tennis Club"
    email = "temp-signup@mergington.edu"

    # Ensure clean state
    if email in activities[activity]["participants"]:
        activities[activity]["participants"].remove(email)

    # Sign up
    resp = client.post(f"/activities/{activity}/signup?email={email}")
    assert resp.status_code == 200

    # Fetch activities and check participant present
    resp2 = client.get("/activities")
    assert email in resp2.json()[activity]["participants"]

    # Cleanup
    if email in activities[activity]["participants"]:
        activities[activity]["participants"].remove(email)
