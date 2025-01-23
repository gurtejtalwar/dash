from pydantic import BaseModel
from typing import Optional

class ChabotMeta(BaseModel):
    is_voice: Optional[bool]
    is_active: Optional[bool]
    is_public: Optional[bool]
    is_deleted: Optional[bool]
    is_favorite: Optional[bool]
    

class ChatbotBase(BaseModel):
    name: str
    owner_id: str

class ChatbotIn(ChatbotBase):
    
    description: Optional[str] = None
    knowledge_base_id: Optional[str] = None
    meta: Optional[ChabotMeta] = None
