import pytest
import requests


@pytest.fixture(scope="session")
def no_auth_session():
    with requests.Session() as session:
        yield session
