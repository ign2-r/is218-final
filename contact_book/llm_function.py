from dotenv import load_dotenv
import os
import requests
from sqlalchemy.orm import sessionmaker
from models import Contact
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = "sqlite:///contacts.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

# Groq API Key and Endpoint
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")
API_URL = "https://api.groq.com/v1/chat/completions"

# Retrieve a contact by name
def get_contact(name):
    session = SessionLocal()
    contact = session.query(Contact).filter_by(name=name).first()
    session.close()
    if contact:
        return {"name": contact.name, "phone": contact.phone}
    return {"error": f"Contact {name} not found."}

# Add a new contact
def add_contact(name, phone):
    session = SessionLocal()
    if session.query(Contact).filter_by(name=name).first():
        session.close()
        return {"error": f"Contact {name} already exists."}
    new_contact = Contact(name=name, phone=phone)
    session.add(new_contact)
    session.commit()
    session.close()
    return {"message": f"Contact {name} added successfully."}

# Example LLM function calling
def function_call_example():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    # Send a request to Groq
    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "model": "llama2-70b-chat",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is John Doe’s phone number?"}
            ],
            "functions": [
                {
                    "name": "get_contact",
                    "description": "Retrieve a contact's phone number by name.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "The contact's name"}
                        },
                        "required": ["name"]
                    }
                }
            ],
            "function_call": {"name": "get_contact"}
        },
    )

    # Parse the response
    if response.status_code == 200:
        result = response.json()["choices"][0]["message"]["function_call"]["arguments"]
        return get_contact(result["name"])
    else:
        return {"error": "Failed to communicate with Groq API."}

if __name__ == "__main__":
    print(function_call_example())