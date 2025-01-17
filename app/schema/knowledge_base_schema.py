from pydantic import BaseModel

from app.models.knowledge_base_models import KnowledgeBaseTypes, KnowledgeBaseModels

class KnowledgeBaseIn(BaseModel):
    name: str
    owner_id: str
    type: KnowledgeBaseTypes
    model: KnowledgeBaseModels

