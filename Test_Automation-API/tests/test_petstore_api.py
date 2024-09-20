import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
PET_ENDPOINT = f"{BASE_URL}/pet"

# Sample pet data for tests
new_pet = {
    "id": 12345,
    "category": {"id": 1, "name": "Dogs"},
    "name": "Bulldog",
    "photoUrls": ["https://example.com/dog.jpg"],
    "tags": [{"id": 1, "name": "bulldog"}],
    "status": "available"
}

updated_pet = {
    "id": 12345,
    "category": {"id": 1, "name": "Dogs"},
    "name": "UpdatedBulldog",
    "photoUrls": ["https://example.com/dog_updated.jpg"],
    "tags": [{"id": 1, "name": "bulldog"}],
    "status": "sold"
}


# Helper function to create a pet
def create_pet(pet_data):
    return requests.post(PET_ENDPOINT, json=pet_data)

# Helper function to get a pet by ID
def get_pet(pet_id):
    return requests.get(f"{PET_ENDPOINT}/{pet_id}")

# Helper function to update a pet
def update_pet(pet_data):
    return requests.put(PET_ENDPOINT, json=pet_data)

# Helper function to delete a pet
def delete_pet(pet_id):
    return requests.delete(f"{PET_ENDPOINT}/{pet_id}")


### Positive Test Cases ###

# Test case to create a new pet (positive scenario)
def test_create_pet_positive():
    response = create_pet(new_pet)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_data = response.json()
    assert response_data["id"] == new_pet["id"], "Pet ID does not match"
    assert response_data["name"] == new_pet["name"], "Pet name does not match"

# Test case to read pet data by ID (positive scenario)
def test_read_pet_positive():
    response = get_pet(new_pet["id"])
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_data = response.json()
    assert response_data["id"] == new_pet["id"], "Pet ID does not match"
    assert response_data["name"] == new_pet["name"], "Pet name does not match"

# Test case to update a pet (positive scenario)
def test_update_pet_positive():
    response = update_pet(updated_pet)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_data = response.json()
    assert response_data["name"] == updated_pet["name"], "Pet name was not updated"
    assert response_data["status"] == updated_pet["status"], "Pet status was not updated"

# Test case to delete a pet by ID (positive scenario)
def test_delete_pet_positive():
    response = delete_pet(new_pet["id"])
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_data = response.json()
    assert response_data["message"] == str(new_pet["id"]), "Pet was not deleted"

# Test case to verify pet is deleted (read after deletion)
def test_read_pet_after_deletion():
    response = get_pet(new_pet["id"])
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    response_data = response.json()
    assert response_data["message"] == "Pet not found", "Deleted pet still exists"

### Negative Test Cases ###

# Test case to create a pet with missing required fields (negative scenario)
def test_create_pet_missing_required_fields_negative():
    incomplete_pet = {
        "id": 67890,
        "category": {"id": 1, "name": "Cats"}
        # Missing "name" and "status"
    }
    response = create_pet(incomplete_pet)
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"

# Test case to read a non-existent pet (negative scenario)
def test_read_nonexistent_pet_negative():
    nonexistent_pet_id = 99999999
    response = get_pet(nonexistent_pet_id)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    response_data = response.json()
    assert response_data["message"] == "Pet not found", "Error message for non-existent pet is incorrect"

# Test case to update a non-existent pet (negative scenario)
def test_update_nonexistent_pet_negative():
    nonexistent_pet = {
        "id": 99999999,
        "category": {"id": 1, "name": "Dogs"},
        "name": "GhostDog",
        "photoUrls": ["https://example.com/ghost.jpg"],
        "tags": [{"id": 1, "name": "ghost"}],
        "status": "available"
    }
    response = update_pet(nonexistent_pet)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"

# Test case to delete a non-existent pet (negative scenario)
def test_delete_nonexistent_pet_negative():
    nonexistent_pet_id = 99999999
    response = delete_pet(nonexistent_pet_id)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    response_data = response.json()
    assert response_data["message"] == "Pet not found", "Error message for non-existent pet is incorrect"


