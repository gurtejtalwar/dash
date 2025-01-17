from crawl4ai import *
from contextlib import asynccontextmanager
from fastapi import FastAPI
import logfire

from app.db import init_db, close_db
from app.routers.knowledge_base_api import router as knowledge_base_router
from app.routers.kb_resource_api import router as kb_resource_router

logfire.configure()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI application.
    Handles database connection lifecycle.
    """
    try:
        init_db()
        yield
    finally:
        close_db()

app = FastAPI(lifespan=lifespan)
logfire.instrument_fastapi(app)
logfire.instrument_pymongo()

app.include_router(knowledge_base_router, tags=["KnowledgeBase"])
app.include_router(kb_resource_router, tags=["KbResource"])
