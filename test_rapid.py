# import pytest
# import requests
# from unittest.mock import patch

# def fetch_company_jobs():
#     url = "https://linkedin-data-api.p.rapidapi.com/company-jobs"

#     payload = {
#         "companyIds": [5383240, 2382910],
#         "page": 1
#     }
#     headers = {
#         "x-rapidapi-key": "60afc02605mshab12b14c209bc06p1f1362jsn69570887ce1f",
#         "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
#         "Content-Type": "application/json"
#     }

#     response = requests.post(url, json=payload, headers=headers)
#     return response.json()

# # Test file (e.g., test_company_jobs.py)
# @patch('requests.post')
# def test_fetch_company_jobs(mock_post):
#     # Define a mock response object with desired attributes
#     mock_response = mock_post.return_value
#     mock_response.json.return_value = {
#         "data": {
#             "jobs": [
#                 {"id": "job1", "title": "Software Engineer"},
#                 {"id": "job2", "title": "Product Manager"}
#             ]
#         }
#     }

#     result = fetch_company_jobs()

#     # Assert that the post request was called with the correct URL, payload, and headers
#     mock_post.assert_called_once_with(
#         "https://linkedin-data-api.p.rapidapi.com/company-jobs",
#         json={
#             "companyIds": [5383240, 2382910],
#             "page": 1
#         },
#         headers={
#             "x-rapidapi-key": "60afc02605mshab12b14c209bc06p1f1362jsn69570887ce1f",
#             "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
#             "Content-Type": "application/json"
#         }
#     )

#     # Assert that the result matches the expected mock response
#     assert result == {
#         "data": {
#             "jobs": [
#                 {"id": "job1", "title": "Software Engineer"},
#                 {"id": "job2", "title": "Product Manager"}
#             ]
#         }
#     }

# if __name__ == "__main__":
#     pytest.main()

import pytest
from unittest.mock import patch
import requests
from rapid import fetch_company_jobs  # Replace 'your_module' with the actual module name

# Test when the API returns a successful response
@patch('requests.post')
def test_fetch_company_jobs_success(mock_post):
    # Mock response object with the desired attributes
    mock_response = mock_post.return_value
    mock_response.json.return_value = {
        "data": {
            "jobs": [
                {"id": "job1", "title": "Software Engineer"},
                {"id": "job2", "title": "Product Manager"}
            ]
        }
    }

    # Call the function
    result = fetch_company_jobs()

    # Verify the post request was made with the correct URL, payload, and headers
    mock_post.assert_called_once_with(
        "https://linkedin-data-api.p.rapidapi.com/company-jobs",
        json={
            "companyIds": [5383240, 2382910],
            "page": 1
        },
        headers={
            "x-rapidapi-key": "60afc02605mshab12b14c209bc06p1f1362jsn69570887ce1f",
            "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
            "Content-Type": "application/json"
        }
    )

    # Assert the result matches the expected mock response
    assert result == {
        "data": {
            "jobs": [
                {"id": "job1", "title": "Software Engineer"},
                {"id": "job2", "title": "Product Manager"}
            ]
        }
    }

# Test when the API returns an error response
@patch('requests.post')
def test_fetch_company_jobs_failure(mock_post):
    # Mock response object to simulate an error
    mock_response = mock_post.return_value
    mock_response.json.return_value = {"error": "Invalid API key"}
    mock_response.status_code = 403

    result = fetch_company_jobs()

    # Assert that the response contains the error message
    assert result == {"error": "Invalid API key"}

# Test when the API is unreachable
@patch('requests.post')
def test_fetch_company_jobs_unreachable(mock_post):
    # Simulate a request exception
    mock_post.side_effect = requests.exceptions.RequestException("API unreachable")

    with pytest.raises(requests.exceptions.RequestException):
        fetch_company_jobs()
