import requests
import logging
from faker import Faker


fake = Faker()


class Pet:
    def __init__(
        self,
        pet_id: int,
        category: dict,
        name: str,
        photo_urls: list[str],
        tags: list[dict],
        status: str
    ):
        self.id = pet_id
        self.category = category
        self.name = name
        self.photoUrls = photo_urls
        self.tags = tags
        self.status = status

    @staticmethod
    def create_single_pet(session: requests.Session, pet_id=None, category=None, name=None, photo_urls=None, tags=None, status=None):

        url_create = "https://petstore.swagger.io/v2/pet"
        if pet_id is None:
            pet_id = fake.random_int(min=5, max=666)
        if category is None:
            category = {
                "id": 0,
                "name": "string"
            }
        if name is None:
            name = fake.name()
        if photo_urls is None:
            photo_urls = ["str"]
        if tags is None:
            tags = [{"id": 0, "name": "string"}]
        if status is None:
            status = "pending"

        request_body_create = {
            "id": pet_id,
            "category": category,
            "name": name,
            "photoUrls": photo_urls,
            "tags": tags,
            "status": status
        }
        response_create = session.post(url_create, json=request_body_create)
        logging.info(response_create)

        return Pet(
            pet_id=pet_id,
            category=category,
            name=name,
            photo_urls=photo_urls,
            tags=tags,
            status=status
        )

    @staticmethod
    def to_dict(item):
        return vars(item)
        # item.__dict__
        # {key: value for key, value in item.__dict__.items()}

    @staticmethod
    def delete_by_id(pet_id, session: requests.Session):
        url_delete = f"https://petstore.swagger.io/v2/pet/{pet_id}"
        response_delete = session.delete(url_delete)
        logging.info(response_delete)

    @staticmethod
    def get_single_pet_by_id(pet_id, session: requests.Session):
        url_to_get = f"https://petstore.swagger.io/v2/pet/{pet_id}"
        response_create_pet = session.get(url_to_get)
        logging.info(response_create_pet)
        return response_create_pet





    # async def delete(self, session: aiohttp.ClientSession):
    #     url_delete = f"/v2/user/{self.username}"
    #     response_delete = await session.delete(url_delete)
    #     logging.info(response_delete)
    #
    # @staticmethod
    # async def delete_by_username(username: str, session: aiohttp.ClientSession):
    #     url_delete = f"/v2/user/{username}"
    #     response_delete = await session.delete(url_delete)
    #     logging.info(response_delete)
    #
    # @staticmethod
    # async def log_user_out_of_the_system(session: aiohttp.ClientSession):
    #     url_logout = f"/v2/user/logout"
    #     response_logout = await session.get(url_logout)
    #     logging.info(response_logout)
    #
    # @staticmethod
    # async def log_user_in_the_system(username: str, password: str, session: aiohttp.ClientSession):
    #     url_logout = f"/v2/user/login/?username={username}&password={password}"
    #     response_logout = await session.get(url_logout)
    #     logging.info(response_logout)