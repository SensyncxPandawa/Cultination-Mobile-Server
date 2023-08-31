from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from api_analytics.fastapi import Analytics

from app.api.users_auth.router import router as users_auth_router
from app.api.users_class.router import router as users_class_router
from app.api.users_market.router import router as users_market_router
from app.api.users_address.router import router as users_address_router
from app.api.harvest_plan.router import router as harvest_plan_router
from app.api.community_cache.router import router as community_cache_router
from app.api.enum.router import router as enum_router

from .database import get_db, engine
from .admin.sqladmin import create_admin

description = """
Cultination API Server is a component of a larger system designed to provide trading services for aquaculture farmers. This API server provides a way to interact with the system programmatically.
"""

def create_app():
    app = FastAPI(
        title="Cultination API Server",
        description=description,
        version="0.0.1",
        contact={
            "name": "Yahya Aqrom",
            "url": "https://yahyaqr.github.io/",
            "email": "aqrom.yahya75@gmail.com",
        },
    )

    # Enable CORS via middleware
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_headers=['*'],
        allow_methods=['*'],
        allow_origins=['*'],
    )

    # Enable API Analytics
    app.add_middleware(Analytics, api_key="1de3e66a-7bc3-4053-80c7-dc1d6afc2577")

    app.include_router(users_auth_router)
    app.include_router(users_class_router)
    app.include_router(users_market_router)
    app.include_router(users_address_router)
    app.include_router(harvest_plan_router)
    app.include_router(community_cache_router)
    app.include_router(enum_router)

    create_admin(app, engine)

    return app

app = create_app()

@app.get("/", tags=["Debug"], include_in_schema=False)
def check_db_and_go_to_admin(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        response_message = "Database is accessible"
        print(response_message)
        return RedirectResponse(url="/admin")
    except OperationalError as e:
        error_message = f"Database connection error: {str(e)}"
        print(error_message)
        return

