import pytest
from api.pet import PetAPI, Pet

@pytest.fixture
def new_pet():
    return Pet(
        pet_id=12345,
        name="Bulldog",
        category_id=1,
        category_name="Dogs",
        photo_urls=["https://example.com/dog.jpg"],
        tags=[(1, "bulldog")],
        status="available"
    ).to_dict()

@pytest.fixture
def updated_pet():
    return Pet(
        pet_id=12345,
        name="UpdatedBulldog",
        category_id=1,
        category_name="Dogs",
        photo_urls=["https://example.com/dog_updated.jpg"],
        tags=[(1, "bulldog")],
        status="sold"
    ).to_dict()

@pytest.fixture
def nonexistent_pet_id():
    return 99999999

@pytest.fixture
def nonexistent_pet(nonexistent_pet_id):
    return Pet(
        pet_id=nonexistent_pet_id,
        name="GhostDog",
        category_id=1,
        category_name="Dogs",
        photo_urls=["https://example.com/ghost.jpg"],
        tags=[(1, "ghost")],
        status="available"
    ).to_dict()

### Positive Test Cases ###

def test_create_pet_positive(new_pet):
    response = PetAPI.create_pet(new_pet)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()["id"] == new_pet["id"]

def test_read_pet_positive(new_pet):
    PetAPI.create_pet(new_pet)
    response = PetAPI.get_pet(new_pet["id"])
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()["name"] == new_pet["name"]

def test_update_pet_positive(updated_pet):
    response = PetAPI.update_pet(updated_pet)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()["name"] == updated_pet["name"]
    assert response.json()["status"] == updated_pet["status"], "Pet status was not updated"

def test_delete_pet_positive(new_pet):
    PetAPI.create_pet(new_pet)
    response = PetAPI.delete_pet(new_pet["id"])
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert PetAPI.get_pet(new_pet["id"]).status_code == 404


def test_delete_pet_positive(new_pet):
    PetAPI.create_pet(new_pet)
    response = PetAPI.delete_pet(new_pet["id"])
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

def test_read_pet_after_deletion(new_pet):
    PetAPI.create_pet(new_pet)
    PetAPI.delete_pet(new_pet["id"])
    response = PetAPI.get_pet(new_pet["id"])
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    assert response.json()["message"] == "Pet not found"


### Negative Test Cases ###

def test_create_pet_missing_required_fields_negative():
    incomplete_pet = {
        "id": 67890,
        "category": {"id": 1, "name": "Cats"}
        # Missing "name" and "status"
    }
    response = PetAPI.create_pet(incomplete_pet)
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"

def test_read_nonexistent_pet_negative(nonexistent_pet_id):
    response = PetAPI.get_pet(nonexistent_pet_id)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    assert response.json()["message"] == "Pet not found"

def test_update_nonexistent_pet_negative(nonexistent_pet):
    response = PetAPI.update_pet(nonexistent_pet)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"

def test_delete_nonexistent_pet_negative(nonexistent_pet_id):
    response = PetAPI.delete_pet(nonexistent_pet_id)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    assert response.json()["message"] == "Pet not found"
