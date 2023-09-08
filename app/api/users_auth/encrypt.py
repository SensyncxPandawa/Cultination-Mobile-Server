from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_hashed_password(password: str) -> str:
    return await pwd_context.hash(password)

async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return await pwd_context.verify(plain_password, hashed_password)

