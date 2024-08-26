# import pytest
# import requests

# def get_ip_address():
#     url = "https://api.ipify.org/?format=json"
#     response = requests.get(url)
#     return response.json()

# def test_get_ip_address(requests_mock):
#     url = "https://api.ipify.org/?format=json"
#     mock_response = {
#         "ip":"171.76.83.37"
#     }
#     requests_mock.get(url, json=mock_response)

# result = get_ip_address()
# assert result["ip"] == "171.76.83.37"

# import pytest
# import requests

# # Function to be tested
# def get_ip_address():
#     url = "https://api.ipify.org/?format=json"
#     response = requests.get(url)
#     return response.json()

# # Test case
# def test_get_ip_address(requests_mock):
#     url = "https://api.ipify.org/?format=json"
#     mock_response = {
#         "ip": "171.76.83.37"
#     }
#     requests_mock.get(url, json=mock_response)
    
#     # Call the function
#     result = get_ip_address()
    
#     # Assertion
#     assert result["ip"] == "171.76.83.37"

# if __name__ == "__main__":
#     pytest.main()

import pytest
import requests

# Function to be tested
def get_ip_address():
    url = "https://api.ipify.org/?format=json"
    response = requests.get(url)
    return response.json()

# Test case
def test_get_ip_address(requests_mock):
    url = "https://api.ipify.org/?format=json"
    mock_response = {
        "ip": "171.76.83.37"
    }
    requests_mock.get(url, json=mock_response)
    
    # Call the function
    result = get_ip_address()
    
    # Assertion
    assert result["ip"] == "171.76.83.37"

# # Ensure the test function is executed
# if __name__ == "__main__":
#     pytest.main()
