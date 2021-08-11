import requests
import pytest
from Lib.assertions import Assertions
from datetime import datetime
import time


class TestUserRegister:
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    @pytest.mark.parametrize('password, username, firstName, lastName, nameexp', [
        ("123", "learnqa", "learnqa", "learnqa", "Norma"),
        ("", "learnqa", "learnqa", "learnqa", "Dont password"),
        ("123", "", "learnqa", "learnqa", "Dont username"),
        ("123", "learnqa", "", "learnqa", "Dont firstName"),
        ("123", "learnqa", "learnqa", "", "Dont lastName"),
        ("123", "l", "learnqa", "learnqa", "Short username"),
        ("123",
         "qwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuioppqwrtyuiopp",
         "learnqa", "learnqa", "Long username")
    ])



    def test_create_user_with_existing_email(self, password, username, firstName, lastName, nameexp):
        data = {
            'password': password,
            'username': username,
            'firstName': firstName,
            'lastName': lastName,
            'email': self.email}

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_code_status(response, 200)

        time.sleep(2)

        print(nameexp)

        print(response.json(), response.status_code)