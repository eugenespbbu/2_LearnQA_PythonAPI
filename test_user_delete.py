import requests

class TestUserDelete:
    data = {
        'email': 'vinkotov@example.com',
        'password': '1234'
    }

    response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

    assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
    assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
    assert "user_id" in response1.json(), "There is no user id in the response"

    auth_sid = response1 = response1.cookies.get("auth_sid")
    token = response1.headers.get("x-csrf-token")
    user_id_from_auth_method = response1.headers.get("user_id")

    response2 = requests.delete(
        "https://playground.learnqa.ru/api/user/2",
        headers={"x-csrf-token": token},
        cookies={"auth_sid": auth_sid}
    )

    print(response2.text)

