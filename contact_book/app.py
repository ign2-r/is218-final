from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Contact

DATABASE_URL = "sqlite:///contacts.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

# Create the database and seed it with sample data
def init_db():
    Base.metadata.create_all(engine)
    inspector = inspect(engine)
    if not inspector.has_table("contacts"):
        session = SessionLocal()
        session.add_all([
            Contact(name="John Doe", phone="123-456-7890"),
            Contact(name="Jane Smith", phone="987-654-3210")
        ])
        session.commit()
        session.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized and seeded with contacts.")
