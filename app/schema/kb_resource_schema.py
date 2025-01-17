from pydantic import BaseModel
from datetime import datetime

from app.models.knowledge_base_models import KbResourceTypes, KbResourceStatuses

class Content(BaseModel):
    file_name: str
    file_path: str
    question: str
    answer: str
    link: str

class KBResourceIn(BaseModel):
    type: KbResourceTypes
    content: Content
    status: KbResourceStatuses
    knowledge_base_id: str