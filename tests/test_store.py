import logging
import random
from datetime import datetime

import requests

from api_models.store import Store


class TestStore:
    base_url = "https://petstore.swagger.io/v2/store"

    def test_place_an_order_for_pet(
        self,
        no_auth_session: requests.Session,
    ):
        store_request_body_create = {
            "id": random.randint(1, 10),
            "petId": 0,
            "quantity": 0,
            "shipDate": "2024-02-19T16:43:04.637Z",
            "status": "placed",
            "complete": True
        }

        response_create = no_auth_session.post(f"{self.base_url}/order", json=store_request_body_create)
        response_create_json = response_create.json()
        logging.info(response_create)

        get_created_order = Store.get_single_order_by_id(response_create_json["id"], no_auth_session)
        created_order_json = get_created_order.json()
        logging.info(get_created_order)
        # clean up
        Store.delete_order_by_id(response_create_json['id'], no_auth_session)
        # assert
        assert response_create_json['id'] == created_order_json["id"]
        assert response_create_json["petId"] == created_order_json["petId"]
        assert response_create_json["quantity"] == created_order_json["quantity"]
        assert response_create_json["shipDate"] == created_order_json["shipDate"]
        assert response_create_json["status"] == created_order_json["status"]
        assert response_create_json["complete"] == created_order_json["complete"]
        assert response_create.status_code == 200

    def test_find_purchase_order_by_id(
        self,
        no_auth_session: requests.Session,
    ):
        create_order = Store.create_single_order(no_auth_session)

        response_create = no_auth_session.get(f"{self.base_url}/order/{create_order.id}")
        # Store.get_single_order_by_id(create_order.id, no_auth_session)
        created_order_json = response_create.json()
        # assert
        assert created_order_json["id"] == create_order.id
        assert created_order_json["petId"] == create_order.petId
        assert created_order_json["quantity"] == create_order.quantity
        assert datetime.strptime(created_order_json["shipDate"], '%Y-%m-%dT%H:%M:%S.%f%z') == datetime.strptime(
            create_order.shipDate, '%Y-%m-%dT%H:%M:%S.%f%z')
        assert created_order_json["status"] == create_order.status
        assert created_order_json["complete"] == create_order.complete
        assert response_create.status_code == 200


