from fastapi import APIRouter

from app.schema.kb_resource_schema import KBResourceIn
from app.services import kb_resource_service

router = APIRouter(prefix="/v1/kbResource")

@router.get('/{kbResourceId}/{ownerId}')
async def get_kb_resource_by_id(kb_resource_id: str, owner_id: str):
    return await kb_resource_service.get_kb_resource_by_id(kb_resource_id)

@router.get('/knowledgeBase/{knowledgeBaseId}/{ownerId}')
async def get_all_kb_resources_by_knowledge_base(knowledge_base_id: str, owner_id: str):
    return await kb_resource_service.get_kb_resources_by_knowledge_base(knowledge_base_id)

@router.get('owner/{ownerId}')
async def get_all_kb_resources_by_owner(owner_id: str):
    return await kb_resource_service.get_kb_resources_by_owner(owner_id)
    
@router.post('/{ownerId}')
async def create_kb_resource(kb_resource: KBResourceIn):
    return await kb_resource_service.create_kb_resource(kb_resource)