from fastapi import APIRouter
from fastui import FastUI, AnyComponent

from app.schema.knowledge_base_schema import KnowledgeBaseIn
from app.services import knowledge_base_service

router = APIRouter(prefix="/v1/knowledgeBase")

@router.get('/{knowledeBaseId}/{ownerId}')
async def get_knowledge_base_by_id(knowledge_base_id: str, owner_id: str):
    return True #TODO

@router.get('/{ownerId}')
async def get_all_knowledge_bases_by_owner(owner_id: str):
    return True #TODO

@router.post('/{ownerId}')
async def create_knowledge_base(knowledge_base: KnowledgeBaseIn):
    return await knowledge_base_service.create_knowledge_base(knowledge_base)