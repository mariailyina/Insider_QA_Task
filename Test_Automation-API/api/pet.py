import requests

BASE_URL = "https://petstore.swagger.io/v2"
PET_ENDPOINT = f"{BASE_URL}/pet"

class PetAPI:
    @staticmethod
    def create_pet(pet_data):
        return requests.post(PET_ENDPOINT, json=pet_data)

    @staticmethod
    def get_pet(pet_id):
        return requests.get(f"{PET_ENDPOINT}/{pet_id}")

    @staticmethod
    def update_pet(pet_data):
        return requests.put(PET_ENDPOINT, json=pet_data)

    @staticmethod
    def delete_pet(pet_id):
        return requests.delete(f"{PET_ENDPOINT}/{pet_id}")


class Pet:
    def __init__(self, pet_id, name, category_id, category_name, photo_urls, tags, status):
        self.pet_id = pet_id
        self.name = name
        self.category = {"id": category_id, "name": category_name}
        self.photo_urls = photo_urls
        self.tags = [{"id": tag_id, "name": tag_name} for tag_id, tag_name in tags]
        self.status = status

    def to_dict(self):
        return {
            "id": self.pet_id,
            "category": self.category,
            "name": self.name,
            "photoUrls": self.photo_urls,
            "tags": self.tags,
            "status": self.status
        }
