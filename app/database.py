import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

DB_USER = "alembic"
DB_PASS = "thisisalembic"
DB_NAME = "bertambak"

# Set the environment variables
os.environ["DB_USER"] = DB_USER
os.environ["DB_PASS"] = DB_PASS
os.environ["DB_NAME"] = DB_NAME

# Construct the SQLAlchemy connection URL for local PostgreSQL
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}"

# Create the SQLAlchemy engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Reflect existing tables (optional)
metadata = MetaData()
metadata.reflect(bind=engine)

# Bind metadata objects of your models
metadata.bind = engine
metadata.reflect(bind=engine, only=[
    "users_auth",
    "users_2fa",
    "users_class",
    "users_ponds_address",
    "users_primary_address",
    "users_harvest_plan",
    "overview_community_cache",
])

# Create the tables
metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
