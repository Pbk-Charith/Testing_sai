import pytest
from api import app1

@pytest.fixture
def client():
    # Set up the Flask test client
    with app1.test_client() as client:
        yield client

def test_greet(client):
    # Send a GET request to the /api/greet route
    response = client.get('/api/greet')
    
    # Check that the status code is 404 (OK)
    assert response.status_code == 404
    
    # Check that the Content-Type is application/json
    assert response.content_type == 'application/json'
    
    # Parse the JSON data from the response
    data = response.get_json()
    
    # Check the data in the response
    assert data['message'] == 'Hello, welcome to our API!'

# import pytest
# from api import main_app

# @pytest.fixture()
# def app():
#     app = main_app()
#     app.config.update({
#         "TESTING": True,
#     })

#     # other setup can go here

#     yield app

#     # clean up / reset resources here


# @pytest.fixture()
# def client(app):
#     return app.test_client()


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()

# def test_request_example(client):
#     response = client.get("/home")
#     print(response.data)
    # assert b"API Created" in response.data