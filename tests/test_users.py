from app import schemas


def test_create_user(client):
    response = client.post(
        "/users/",
        json={"email": "deadpool@example.com", "password": "chimichangas4life"},
    )
    assert response.status_code == 201
    data = schemas.UserResponse(**response.json())
    assert data.email == "deadpool@example.com"
    user_id = data.id

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = schemas.UserResponse(**response.json())
    assert data.email == "deadpool@example.com"
    assert data.id == user_id
