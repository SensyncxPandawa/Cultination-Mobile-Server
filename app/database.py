import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# Construct the SQLAlchemy connection URL for local PostgreSQL
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}"

# Example online PostgreSQL using neondb
# SQLALCHEMY_DATABASE_URL = f"postgresql://yahyaqr:SRATDMHd91XI@ep-rough-math-66050287.ap-southeast-1.aws.neon.tech/neondb"

# Create the SQLAlchemy engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Reflect existing tables (optional)
metadata = MetaData()
metadata.reflect(bind=engine)

# Bind metadata objects of your models
metadata.bind = engine
metadata.reflect(bind=engine, only=[
    "community_cache",
    "users_2fa",
    "users_auth",
    "users_class",
    "users_harvest_plan",
    "users_market",
    "users_ponds",
    "users_ponds_address",
    "users_primary_address",
    "kolam_data",
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
