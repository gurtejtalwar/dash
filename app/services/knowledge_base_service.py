from app.schema.knowledge_base_schema import KnowledgeBaseIn

from app.db import knowledge_base_db

async def get_knowledge_base_by_id(knowledge_base_id: str):
    return await knowledge_base_db.get_knowledge_base_by_id(knowledge_base_id)

async def get_all_knowledge_bases_by_owner(owner_id: str):
    return await knowledge_base_db.get_all_knowledge_bases_by_owner(owner_id)
    
async def create_knowledge_base(knowledge_base: KnowledgeBaseIn):
    return await knowledge_base_db.save_knowledge_base(knowledge_base)

async def update_knowledge_base(knowledge_base: KnowledgeBaseIn):
    return await knowledge_base_db.update_knowledge_base(knowledge_base)

async def delete_knowledge_base(knowledge_base_id: str):
    return await knowledge_base_db.delete_knowledge_base(knowledge_base_id)