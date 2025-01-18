import asyncio
from crawl4ai import *
from pydantic import HttpUrl

from app.db import kb_resource_db
from app.models.knowledge_base_models import KbResourceTypes
from app.schema.kb_resource_schema import KBResourceIn
from app.common import crawler

async def get_kb_resource_by_id(kb_resource_id: str):
    return await kb_resource_db.get_kb_resource_by_id(kb_resource_id)

async def get_kb_resources_by_knowledge_base(knowledge_base_id: str):
    return await kb_resource_db.get_kb_resources_by_knowledge_base(knowledge_base_id)

async def get_kb_resources_by_owner(owner_id: str):
    return await kb_resource_db.get_kb_resources_by_owner(owner_id)

async def create_kb_resource(kb_resource: KBResourceIn):
    data = await get_data(kb_resource)
    kb_resource.data = data
    return await kb_resource_db.save_kb_resource(kb_resource)

async def update_kb_resource(kb_resource: KBResourceIn):
    return await kb_resource_db.update_kb_resource(kb_resource)

async def delete_kb_resource(kb_resource_id: str):
    return await kb_resource_db.delete_kb_resource(kb_resource_id)

async def get_data(kb_resource: KBResourceIn):
    type_function_map = {
        KbResourceTypes.url: get_data_from_link,
        KbResourceTypes.qa: get_data_from_qa,
        KbResourceTypes.file: get_data_from_file,
    }
    if kb_resource.type not in KbResourceTypes:
        raise ValueError("Incorrect Kb Resource Type")
    func = type_function_map.get(kb_resource.type)
    if func:
        return await func(kb_resource)
    
    raise ValueError(f"Unsupported Kb Resource Type: {kb_resource.type}")

async def get_data_from_link(kb_resource: KBResourceIn) -> str:
    return await crawler.crawl_link(str(kb_resource.content.link))


async def get_data_from_qa():
    return True #TODO

async def get_data_from_file():
    return True #TODO