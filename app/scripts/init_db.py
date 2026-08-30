from app.database import engine
from app.models import *

from sqlalchemy.orm import configure_mappers

configure_mappers()

from app.database import Base

Base.metadata.create_all(bind=engine)

print("Database initialized.")

