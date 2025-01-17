from pydantic import BaseModel
from typing import Optional

from app.models.knowledge_base_models import KbResourceTypes, KbResourceStatuses

class Content(BaseModel):
    file_name: Optional[str] = None
    file_path: Optional[str] = None
    question: Optional[str] = None
    answer: Optional[str] = None
    link: Optional[str] = None

class KBResourceIn(BaseModel):
    type: KbResourceTypes
    content: Content
    status: KbResourceStatuses