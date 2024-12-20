import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llm_function import get_contact, add_contact

def test_get_contact():
    result = get_contact("Rockwell Dela Rosa")
    assert result["phone"] == "123-456-7890"

def test_add_contact():
    result = add_contact("Daniel", "555-555-5555")
    assert result["message"] == "Contact Daniel added successfully."
    result = get_contact("Daniel")
    assert result["phone"] == "555-555-5555"
