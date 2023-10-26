from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Change the database URL to match your preferred database (e.g., MySQL, PostgreSQL).
DATABASE_URL = "sqlite:///book_manager.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
