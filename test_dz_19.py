import requests
import json
from Lib.base_case import BaseCase
from Lib.assertions import Assertions
from datetime import datetime
from Lib.my_requests import MyRequests
import allure
from .steps import imported_step
import nose


@allure.epic("Authorization cases")
@allure.step
class TestUserRegister(BaseCase):
    def setup(self):
        with nose.allure.step('Шаг 1'):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    @allure.step
    def test_create_user_with_existing_email(self):
        with nose.allure.step('Шаг 2'):
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'a@ba.a'}

        response = MyRequests.post("/user", data=data)

        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_code_status(response, 200)

        print(response.text)


class TestUserGet17(BaseCase):


    @allure.description("This test successfully authorize by email and password")
    @allure.step

    def test_get_user_details_auth_as_same_user(self):
        with nose.allure.step('Шаг 3'):


        response1 = MyRequests.post("/user/login", data={'email': self.email,
            'password': '1234'})

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = requests.get(f"https://playground.learnqa.ru/api/user/7218",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})

        print(response2.text, response2.json())

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)
        print(response2.text, response2.json())

        new_name = "n"

        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/362",
             headers={"x-csrf-token": token},
             cookies={"auth_sid": auth_sid},
             data={"firstname": new_name}
        )

        Assertions.assert_code_status(response3, 200)