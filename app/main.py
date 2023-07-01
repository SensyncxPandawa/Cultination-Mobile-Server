from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

from app.api.xcarts_package.router import router as xcarts_router
from app.api.xcategories_package.router import router as xcategories_router
from app.api.xvendors_package.router import router as xvendors_router
from app.api.xusers_package.router import router as xusers_router
from app.api.xpurchases_package.router import router as xpurchases_router
from app.api.xpurchaseitems_package.router import router as xpurchaseitems_router
from app.api.xproducts_package.router import router as xproducts_router

from .database import get_db, engine
from .sqladmin import create_admin

description = """
PandawaxSensync API Server is a component of a larger system designed to provide e-commerce services for aquaculture farmers. This API server provides a way to interact with the system programmatically.
"""

def create_app():
    app = FastAPI(
        title="PandawaxSensync API Server",
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

    app.include_router(xcarts_router)
    app.include_router(xcategories_router)
    app.include_router(xvendors_router)
    app.include_router(xusers_router)
    app.include_router(xpurchases_router)
    app.include_router(xpurchaseitems_router)
    app.include_router(xproducts_router)

    create_admin(app, engine)

    return app

app = create_app()

@app.get("/", tags=["Debug"], include_in_schema=False)
def check_db_and_go_to_admin(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        response_message = "Database is accessible"
        print(response_message)
        return RedirectResponse(url="/admin")
    except OperationalError as e:
        error_message = f"Database connection error: {str(e)}"
        print(error_message)
        return

