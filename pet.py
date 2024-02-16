import requests
import logging
from faker import Faker


fake = Faker()


class Pet:
    def __init__(
        self,
        id: int,
        category: dict,
        name: str,
        photo_urls: list[str],
        tags: list[dict],
        status: str
    ):
        self.id = id
        self.category = category
        self.name = name
        self.photo_urls = photo_urls
        self.tags = tags
        self.status = status

    @staticmethod
    def create_single_pet(session: requests.Session):
        url_create = "https://petstore.swagger.io/v2/pet"

        id = fake.random_int(min=5, max=666)
        category = {
            "id": 0,
            "name": "string"
          }
        name = fake.name()
        photo_urls = ["str"]
        tags = [{"id": 0, "name": "string"}]
        status = "pending"

        request_body_create = {

                "id": id,
                "category": category,
                "name": name,
                "photo_urls": photo_urls,
                "tags": tags,
                "status": status

        }
        response_create = session.post(url_create, json=request_body_create)
        logging.info(response_create)

        return Pet(
            id=id,
            category=category,
            name=name,
            photo_urls=photo_urls,
            tags=tags,
            status=status
        )

    @staticmethod
    def to_dict(item):
        return {key: value for key, value in item.__dict__.items()}

    @staticmethod
    def delete_by_id(id: str, session: requests.Session):
        url_delete = f"https://petstore.swagger.io/v2/pet/{id}"
        response_delete = session.delete(url_delete)
        logging.info(response_delete)

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