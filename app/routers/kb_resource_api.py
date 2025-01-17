from fastapi import APIRouter

from app.schema.kb_resource_schema import KBResourceIn
from app.services import kb_resource_service

router = APIRouter(prefix="/v1/kbResource")

@router.get('/{kbResource}/{ownerId}')
async def get_kb_resource_by_id(kb_resource_id: str, owner_id: str):
    return True #TODO

@router.get('/{ownerId}')
async def get_all_kb_resources_by_knowledge_base(owner_id: str):
    return True #TODO

@router.get('/{ownerId}')
async def get_all_kb_resources_by_owner(owner_id: str):
    return True #TODO

@router.post('/{ownerId}')
async def create_kb_resource(kb_resource: KBResourceIn):
    return await kb_resource_service.create_kb_resource(kb_resource)