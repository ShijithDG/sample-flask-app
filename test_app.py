import pytest
from app import app  # Import the Flask app from app.py

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client  # This will allow us to use the client in our tests

def test_home(client):
    """Test the home route."""
    response = client.get('/')  
    assert response.status_code == 200  
    assert response.data == b'Welcome to Home!'  

def test_profile(client):
    """Test the profile  route."""
    response = client.get('/profile')  
    assert response.status_code == 200  
    assert response.data == b'This is my profile page' 
