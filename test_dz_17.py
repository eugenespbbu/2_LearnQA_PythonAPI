import requests
import json
from Lib.base_case import BaseCase
from Lib.assertions import Assertions

class TestUserGet(BaseCase):
    new_name = "Changed Name"

    response3 = requests.put(
        f"https://playground.learnqa.ru/api/user/362",
        #headers={"x-csrf-token": token},
        #cookies={"auth_sid": auth_sid},
        data={"firstname": new_name}
    )

    Assertions.assert_code_status(response3, 200)