from pydantic import BaseModel

from app.models.knowledge_base_models import KnowledgeBaseTypes, KnowledgeBaseModels

class KnowledgeBaseBase(BaseModel):
    name: str
    owner_id: str
    type: KnowledgeBaseTypes
    model: KnowledgeBaseModels

class KnowledgeBaseIn(KnowledgeBaseBase):
    description: str

