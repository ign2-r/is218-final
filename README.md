# Contact Book with LLM Integration
---

## Demo Video

[![Watch the Demo](https://img.youtube.com/vi/lXHb464l0s8/0.jpg)](https://youtu.be/lXHb464l0s8)

---
## Description
This project is a contact management application that integrates a database (SQLite) with an LLM (Large Language Model) using the Groq API. The application allows you to:

- Retrieve contact information by name.
- Add new contacts to the database.
- Query the LLM for contact information using natural language.

The project includes:
- Automated database initialization and seeding.
- Unit tests to ensure application functionality.
- A CI pipeline using GitHub Actions.

---

## Features
- **Retrieve Contacts**: Fetch contact details by name.
- **Add Contacts**: Add new contact details to the database.
- **LLM Integration**: Query the contact book using natural language.
- **Automated Testing**: Includes unit tests to validate functionality.
- **CI/CD Pipeline**: Ensures quality with GitHub Actions.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ign2-r/is218-final.git
cd is218-final/contact_book
```

### 2. Set Up the Environment
1. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up a `.env` file for the Groq API key:
   ```plaintext
   GROQ_API_KEY=your_actual_api_key
   ```

### 3. Initialize the Database
Run the `app.py` script to create and seed the database:
```bash
python app.py
```

---

## Usage

### 1. Run the Application
To query the LLM for contact information:
```bash
python llm_function.py
```

### 2. Run Unit Tests
To verify the application functionality:
```bash
pytest tests/
```

---

## CI/CD Pipeline
This project includes a GitHub Actions workflow:
- **Triggers**: The pipeline runs on every push and pull request to the `main` branch.
- **Steps**:
  1. Set up the Python environment.
  2. Install dependencies.
  3. Initialize the database.
  4. Run unit tests using `pytest`.

---

## Docker Support
To run the application using Docker:

### 1. Build the Docker Image
```bash
docker build -t contact_book .
```

### 2. Run the Docker Container
```bash
docker run --env-file .env -it --rm contact_book
```

---

## Project Structure
```
contact_book/
├── app.py               # Database initialization and seeding
├── llm_function.py      # LLM integration and API queries
├── models.py            # SQLAlchemy models for the database
├── requirements.txt     # Project dependencies
├── tests/
│   ├── conftest.py      # Test setup and database initialization
│   ├── test_app.py      # Unit tests for application functionality
├── Dockerfile           # Docker configuration
└── .github/
    └── workflows/
        └── ci.yml       # GitHub Actions workflow
```

---

## Contributing
Feel free to fork this repository, make changes, and submit a pull request.

---

## License
This project is licensed under the MIT License.