import sys
import os

# Add the parent directory (where `app.py` is located) to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import init_db
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # Initialize the database before any tests run
    init_db()
