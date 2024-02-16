import requests
import logging


class TestUser:
    suite_url_suffix = "https://petstore.swagger.io/v2/"

    def test_create_single_user(
        self,
        no_auth_session: requests.Session,
    ):
        test_url_suffix = "https://petstore.swagger.io/v2/user"

        request_body_create = {
                  "id": 0,
                  "username": "JonDoe",
                  "firstName": "Jon",
                  "lastName": "Doe",
                  "email": "JonDoe@gmail.com",
                  "password": "string",
                  "phone": "string",
                  "userStatus": 12
                }

        response_create = no_auth_session.post(test_url_suffix, json=request_body_create)
        logging.info(response_create)
        response_create_json = response_create.json()

        assert response_create.status_code == 200
        assert response_create_json["code"] == 200

    def test_update_single_user(
        self,
        no_auth_session: requests.Session,
    ):
        test_url_suffix = "https://petstore.swagger.io/v2/user/JonDo"

        request_body_create = {
                  "id": 0,
                  "username": "JonDoe",
                  "firstName": "Jon",
                  "lastName": "Doe",
                  "email": "JonDoe@gmail.com",
                  "password": "string",
                  "phone": "string",
                  "userStatus": 0
                }

        response_create = no_auth_session.put(test_url_suffix, json=request_body_create)
        logging.info(response_create)
        response_create_json = response_create.json()

        assert response_create.status_code == 200
        assert response_create_json["code"] == 200

    def test_log_in_single_user(
        self,
        no_auth_session: requests.Session,
    ):
        test_url_suffix = "https://petstore.swagger.io/v2/user/login?username=JonDoe&password=123456"

        response_create = no_auth_session.get(test_url_suffix)
        logging.info(response_create)
        response_create_json = response_create.json()

        assert response_create.status_code == 200
        assert response_create_json["code"] == 200



