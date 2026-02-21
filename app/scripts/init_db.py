import os
from sqlalchemy import create_engine
from app.models import Base

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL)

print("🟢 Creating database tables if not exist...")
Base.metadata.create_all(bind=engine)
print("✅ Database initialized successfully")

