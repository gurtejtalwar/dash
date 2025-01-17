from app.schema.knowledge_base_schema import KnowledgeBaseIn

from app.db.knowledge_base_db import save_knowledge_base

async def create_knowledge_base(knowledge_base: KnowledgeBaseIn, owner_id: str):
    return await save_knowledge_base(knowledge_base)