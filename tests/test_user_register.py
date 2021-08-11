import requests
from Lib.assertions import Assertions
from datetime import datetime


class TestUserRegister:
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}{domain}"

    def test_create_user_with_existing_email(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email}

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_code_status(response, 200)

        print(response.json())