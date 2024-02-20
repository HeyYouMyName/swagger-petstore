import logging
import random
from datetime import datetime, timezone

import requests


class Store:
    base_url = r"https://petstore.swagger.io/v2/store/order"

    def __init__(
        self,
        order_id: int,
        pet_id: int,
        quantity: int,
        ship_date: str,
        status: str,
        complete: bool
    ):
        self.id = order_id
        self.petId = pet_id
        self.quantity = quantity
        self.shipDate = ship_date
        self.status = status
        self.complete = complete

    @staticmethod
    def create_single_order(session: requests.Session, order_id=None, pet_id=None, quantity=None, ship_date=None, status=None, complete=None):
        url_create = Store.base_url
        current_datetime = datetime.now(timezone.utc)
        if order_id is None:
            order_id = random.randint(1, 10)
        if pet_id is None:
            pet_id = random.randint(1, 10)
        if quantity is None:
            quantity = random.randint(1, 10)
        if ship_date is None:
            ship_date = current_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + current_datetime.strftime('%z')  # this is not getting along with this line "Store.generate_random_data()"
        if status is None:
            status = "placed"
        if complete is None:
            complete = True

        request_body_create = {
            "id": order_id,
            "petId": pet_id,
            "quantity": quantity,
            "shipDate": ship_date,
            "status": status,
            "complete": complete
        }
        response_create = session.post(url_create, json=request_body_create)
        logging.info(response_create)

        return Store(
            order_id=order_id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete
        )

    @staticmethod
    def get_single_order_by_id(store_id, session: requests.Session):
        url_to_get = f"{Store.base_url}/{store_id}"
        response_create_store = session.get(url_to_get)
        logging.info(response_create_store)
        return response_create_store

    @staticmethod
    def delete_order_by_id(store_id, session: requests.Session):
        url_delete = f"{Store.base_url}/{store_id}"
        response_delete = session.delete(url_delete)
        logging.info(response_delete)
