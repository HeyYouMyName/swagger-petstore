import requests
import logging
from pet import Pet


class TestPet:
    base_url = "https://petstore.swagger.io/v2/pet/"
    list_of_status = ["available", "pending", "sold"]

    def test_update_pet(
        self,
        no_auth_session: requests.Session,
        name_to_change="hopelessness"
    ):
        create_pet = Pet.create_single_pet(no_auth_session)

        get_created_pet = no_auth_session.get(f"{self.base_url}{create_pet.id}")
        created_pet_json = get_created_pet.json()

        create_pet.name = name_to_change
        response_create = no_auth_session.put(f"{self.base_url}", json=Pet.to_dict(create_pet))
        logging.info(response_create)

        get_updated_pet = no_auth_session.get(f"{self.base_url}{create_pet.id}")
        updated_pet_json = get_updated_pet.json()

        # assert
        assert response_create.status_code == 200
        assert updated_pet_json["id"] == created_pet_json["id"]
        assert updated_pet_json["name"] != created_pet_json["name"]
        # clean up
        Pet.delete_by_id(updated_pet_json["id"], no_auth_session)

    def test_add_new_pet_to_store(
        self,
        no_auth_session: requests.Session,
        faker
    ):
        request_body_create = {
                      "id": faker.random_int(min=5, max=666),
                      "category": {
                        "id": 0,
                        "name": "string"
                      },
                      "name": "FussRoDah",
                      "photoUrls": [
                        "string"
                      ],
                      "tags": [
                        {
                          "id": 0,
                          "name": "string"
                        }
                      ],
                      "status": self.list_of_status[1]
                    }

        response_create = no_auth_session.post(self.base_url, json=request_body_create)
        response_create_json = response_create.json()
        logging.info(response_create)

        get_created_pet = no_auth_session.get(f"{self.base_url}{response_create_json['id']}")
        created_pet_json = get_created_pet.json()
        logging.info(get_created_pet)

        assert response_create_json['id'] == created_pet_json["id"]
        assert response_create.status_code == 200
        # clean up
        Pet.delete_by_id(response_create_json['id'], no_auth_session)

    def test_find_pet_by_status(
        self,
        no_auth_session: requests.Session,
    ):
        response_create = no_auth_session.get(self.base_url + "findByStatus?status=" + self.list_of_status[1])
        logging.info(response_create)
        response_create_json = response_create.json()
        for pet in response_create_json:
            assert self.list_of_status[1] == pet["status"]
        assert response_create.status_code == 200




    # def test_clean_up_after_everyone_pet_by_status(
    #     self,
    #     no_auth_session: requests.Session,
    # ):
    #     test_url_suffix = "https://petstore.swagger.io/v2/pet/findByStatus?status=sold"
    #
    #
    #
    #     response_create = no_auth_session.get(test_url_suffix)
    #     logging.info(response_create)
    #     response_create_json = response_create.json()
    #     print(response_create_json)
    #     for i in response_create_json:
    #         no_auth_session.delete(self.base_url + str(i["id"]))
    #     assert response_create.status_code == 200

