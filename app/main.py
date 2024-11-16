"""This module contains the main FastAPI application."""

from contextlib import asynccontextmanager

from anyio import to_thread
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse

# from app.core.database import initialize_tables
# from app.item.models import MODULE_TABLES as item_models

# Globals
# TABLES = {**item_models}


# Lifespan (startup, shutdown)
@asynccontextmanager
async def lifespan(_: FastAPI):
    """This is the startup and shutdown code for the FastAPI application."""
    # Startup code
    print("System Call: Enhance Armament x_x")  # SAO Reference

    # Bigger Threadpool i.e you send a bunch of requests it will handle a max of 1000 at a time, the default is 40
    limiter = to_thread.current_default_thread_limiter()
    limiter.total_tokens = 1000

    # Init tables
    # initialize_tables(tables_dict=TABLES)

    # Shutdown
    yield
    print("System Call: Release Recollection...")


app = FastAPI(
    title="Heavyweight(FastAPI)",
    docs_url="/",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1
    },  # Hides Schemas Menu in Docs
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

# Variables
origins = ["*"]

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    GZipMiddleware,
    minimum_size=5000,  # Minimum size of the response before it is compressed in bytes
)


# Health Check
@app.get("/health", status_code=200, include_in_schema=False)
async def health_check():
    """This is the health check endpoint"""
    return {"status": "ok"}


# Routers
