import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# Construct the SQLAlchemy connection URL for local PostgreSQL
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}"

# Create the asynchronous SQLAlchemy engine and session
async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_sessionmaker = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Dependency
def get_db():
    db = async_sessionmaker()
    try:
        yield db
    finally:
        db.close()
