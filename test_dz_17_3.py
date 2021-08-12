import requests
import json
from Lib.base_case import BaseCase
from Lib.assertions import Assertions
from datetime import datetime

class TestUserRegister:
    #def setup(self):
        #base_part = "learnqa"
        #domain = "example.com"
        #random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        #self.email = f"{base_part}{random_part}@{domain}"


    def test_create_user_with_existing_email(self):
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'b@b.r'}

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_code_status(response, 200)
        print(response.text)

class TestUserGet17(BaseCase):


    def test_get_user_details_auth_as_same_user(self):


        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data={'email': 'b@b.r',
            'password': '1234'})

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = requests.get(f"https://playground.learnqa.ru/api/user/2",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})

        print(response2.text, response2.json())



        new_name = "Changed Name"

        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/7218",
             headers={"x-csrf-token": token},
             cookies={"auth_sid": auth_sid},
             data={"email": 'kdkd.ru'}
        )

        Assertions.assert_code_status(response3, 200)