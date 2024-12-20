from llm_function import get_contact, add_contact

# Test retrieving an existing contact
def test_get_contact():
    result = get_contact("Rockwell Dela Rosa")
    assert "phone" in result, f"Expected 'phone' key in result, got: {result}"
    assert result["phone"] == "123-456-7890"

# Test adding a new contact
def test_add_contact():
    result = add_contact("Daniel", "555-555-5555")
    assert result["message"] == "Contact Daniel added successfully."
    # Verify the contact was added
    result = get_contact("Daniel")
    assert "phone" in result, f"Expected 'phone' key in result, got: {result}"
    assert result["phone"] == "555-555-5555"

# Test retrieving a non-existent contact
def test_get_missing_contact():
    result = get_contact("Nonexistent Contact")
    assert "error" in result, f"Expected 'error' key in result, got: {result}"
    assert result["error"] == "Contact Nonexistent Contact not found."
