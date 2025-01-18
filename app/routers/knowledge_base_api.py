from fastapi import APIRouter
from fastui import FastUI, AnyComponent

from app.schema.knowledge_base_schema import KnowledgeBaseIn
from app.services import knowledge_base_service

router = APIRouter(prefix="/v1/knowledgeBase")

@router.get('/{knowledeBaseId}/{ownerId}')
async def get_knowledge_base_by_id(knowledge_base_id: str, owner_id: str):
    return knowledge_base_service.get_knowledge_base_by_id(knowledge_base_id)
    
@router.get('/{ownerId}')
async def get_all_knowledge_bases_by_owner(owner_id: str):
    return knowledge_base_service.get_all_knowledge_bases_by_owner(owner_id)

@router.post('/{ownerId}')
async def create_knowledge_base(knowledge_base: KnowledgeBaseIn):
    return await knowledge_base_service.create_knowledge_base(knowledge_base)

@router.put('/{ownerId}')
async def update_knowledge_base(knowledge_base: KnowledgeBaseIn):
    return await knowledge_base_service.update_knowledge_base(knowledge_base)

@router.delete('/{knowledgeBaseId}/{ownerId}')
async def delete_knowledge_base(knowledge_base_id: str, owner_id: str):
    return await knowledge_base_service.delete_knowledge_base(knowledge_base_id)