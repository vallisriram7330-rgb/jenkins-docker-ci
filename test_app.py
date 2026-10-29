from app import greet

def test_greet():
    assert greet() == "Hello from the CI/CD pipeline!"