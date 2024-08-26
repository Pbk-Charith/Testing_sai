import requests
import pytest

# Function to make the API call
def get_age_prediction(count):
    url = f"https://api.agify.io/?count={count}"
    response = requests.get(url)
    return response.json()

# Test case using requests-mock
def test_get_age_prediction(requests_mock):
    # Define the mock URL and response
    url = "https://api.agify.io/?count=20"
    mock_response = {
        "name": "meelad",
        "age": 34,
        "count": 20
    }

    # Set up the mock to intercept the request and return the mock response
    requests_mock.get(url,json=mock_response)

    # Call the function and assert the response
    result = get_age_prediction(20)
    assert result["name"] == "meelad"
    assert result["age"] == 34
    assert result["count"] == 20

# def test_get_age_prediction_invalid_name(requests):
#     # Define the mock URL for an invalid name
#     mock_url = "https://api.agify.io/?name=invalidname"
#     mock_response = {
#         "name": "invalidname",
#         "age": None,
#         "count": 0
#     }

#     # Set up the mock to intercept the request and return the mock response
#     requests.get(mock_url, json=mock_response)

#     # Call the function and assert the response
#     result = get_age_prediction("invalidname")
#     assert result["name"] == "invalidname"
#     assert result["age"] is None
#     assert result["count"] == 0
