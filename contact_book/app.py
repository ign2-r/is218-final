from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Contact
from sqlalchemy import inspect

DATABASE_URL = "sqlite:///contacts.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

# Create the database and seed it with sample data
def init_db():
    # Reset the database
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # Seed the database with test data
    session = SessionLocal()
    session.add_all([
        Contact(name="Rockwell Dela Rosa", phone="123-456-7890"),
        Contact(name="Cole Abney", phone="987-654-3210")
    ])
    session.commit()
    session.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized and seeded with contacts.")
