from pydantic import BaseModel, HttpUrl
from typing import Optional

from app.models.knowledge_base_models import KbResourceTypes, KbResourceStatuses

class Content(BaseModel):
    file_name: Optional[str] = None
    file_path: Optional[str] = None
    question: Optional[str] = None
    answer: Optional[str] = None
    link: Optional[HttpUrl] = None

class KBResourceBase(BaseModel):
    knowledge_base: str
    type: KbResourceTypes
    content: Content
    status: KbResourceStatuses
    data: Optional[str] = None
    
class KBResourceIn(KBResourceBase):
    ...

class KBResourceOut(KBResourceBase):
    data: str