import pytest
from app import init_db

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # Initialize the database before any tests run
    init_db()
