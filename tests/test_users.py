import pytest
from app import schemas, config
from jose import jwt


def test_login_user(client, test_user):
    data = {
        'username': test_user['email'],
        'password': test_user['password']
    }
    response = client.post('/login', data=data)
    login_res = schemas.Token(**response.json())
    payload = jwt.decode(login_res.access_token,
                         config.settings.SECRET_KEY, algorithms=[config.settings.ALGORITHM])
    id = payload.get("user_id")
    assert str(id) == test_user['id']
    assert login_res.token_type == "bearer"
    assert response.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'password123', 403),
    ('sanjeev@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 422),
    ('sanjeev@gmail.com', None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post(
        "/login", data={"username": email, "password": password})

    assert res.status_code == status_code