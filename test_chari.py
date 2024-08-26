import requests 
import pytest

def get_geo_location(postal):
    url = f"https://ipinfo.io/161.185.160.93/postal={postal}"
    response = requests.get(url)
    return response.json()

def test_get_geo_location(requests_mock):
    url = "https://ipinfo.io/161.185.160.93/postal=10001"
    mock_response = {
        "ip": "161.185.160.93",
        "city": "New York City",
        "region": "New York",
        "country": "US",
        "loc": "40.7143,-74.0060",
        "org": "AS22252 The City of New York",
        "postal": 10001,
        "timezone": "America/New_York",
        "readme": "https://ipinfo.io/missingauth"
    }

    requests_mock.get(url, json=mock_response)

    answer = get_geo_location(10001)
    assert answer["ip"] == "161.185.160.93"
    assert answer["city"] == "New York City"
    assert answer["region"] == "New York"
    assert answer["country"] == "US"
    assert answer["loc"] == "40.7143,-74.0060"
    assert answer["org"] == "AS22252 The City of New York"
    assert answer["postal"] == 10001
    assert answer["timezone"] == "America/New_York"
    assert answer["readme"] == "https://ipinfo.io/missingauth"

    # result = get_geo_location()
    # assert result[]
  

# import requests
# import pytest

# def get_geo_location(postal):
#     url = f"https://ipinfo.io/161.185.160.93/postal={postal}"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # This will raise an exception for HTTP errors
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         # Handle any request exceptions (e.g., network issues)
#         return {"error": str(e)}

# # Test case for valid response
# def test_get_geo_location_success(requests_mock):
#     url = "https://ipinfo.io/161.185.160.93/postal=10001"
#     mock_response = {
#         "ip": "161.185.160.93",
#         "city": "New York City",
#         "region": "New York",
#         "country": "US",
#         "loc": "40.7143,-74.0060",
#         "org": "AS22252 The City of New York",
#         "postal": 10001,
#         "timezone": "America/New_York",
#         "readme": "https://ipinfo.io/missingauth"
#     }

#     # Mock the successful response
#     requests_mock.get(url, json=mock_response)

#     answer = get_geo_location(10001)
#     assert answer["ip"] == "161.185.160.93"
#     assert answer["city"] == "New York City"
#     assert answer["region"] == "New York"
#     assert answer["country"] == "US"
#     assert answer["loc"] == "40.7143,-74.0060"
#     assert answer["org"] == "AS22252 The City of New York"
#     assert answer["postal"] == 10001
#     assert answer["timezone"] == "America/New_York"
#     assert answer["readme"] == "https://ipinfo.io/missingauth"

# # Test case for network error
# def test_get_geo_location_network_error(requests_mock):
#     url = "https://ipinfo.io/161.185.160.93/postal=10001"
    
#     # Mock a network error
#     requests_mock.get(url, exc=requests.exceptions.ConnectionError)
    
#     answer = get_geo_location(10001)
#     assert "error" in answer
#     assert "ConnectionError" in answer["error"]

# # Test case for invalid response
# def test_get_geo_location_invalid_response(requests_mock):
#     url = "https://ipinfo.io/161.185.160.93/postal=10001"
    
#     # Mock an invalid response (e.g., a non-JSON response)
#     requests_mock.get(url, text="Not a valid JSON")
    
#     answer = get_geo_location(10001)
#     assert "error" in answer
