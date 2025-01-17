from app.db.kb_resource_db import save_kb_resource
from app.schema.kb_resource_schema import KBResourceIn

async def create_kb_resource(kb_resource: KBResourceIn):
    return await save_kb_resource(kb_resource)