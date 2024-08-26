# import requests
# import k
# import pytest

# # Function to be tested
# def get_cat_fact():
#     url = "https://catfact.ninja/fact"
#     response = requests.get(url)
#     return response.json()

# # Test case
# def test_get_cat_fact(requests_mock):
#     url = "https://catfact.ninja/fact"
#     mock_response = {
#         "fact": "Cats have five toes on their front paws, but only four on the back ones.",
#         "length": 71
#     }
    
#     # Mock the response
#     requests_mock.get(url,json=mock_response)
    
#     # Call the function
#     result = get_cat_fact()
#     assert result["length"] == 71

import requests
import pytest

# Function to be tested
def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    return response.json()

# Test case
def test_get_cat_fact(requests_mock):
    url = "https://catfact.ninja/fact"
    mock_response = {
        "fact": "Cats have five toes on their front paws, but only four on the back ones.",
        "length": 71
    }
    
    # Mock the response
    requests_mock.get(url, json=mock_response)
    
    # Call the function
    result = get_cat_fact()  # Call the function with parentheses
    
    # Assert the length of the cat fact
    assert result["length"] == 71

# To run the coverage report, use the following command in your terminal:
# pytest --cov=test_k --cov-report=term-missing
