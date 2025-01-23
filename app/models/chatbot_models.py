from enum import StrEnum
from mongoengine import (EnumField, StringField, ListField, EmbeddedDocumentField, EmbeddedDocument, BooleanField, DateTimeField, ReferenceField)

from app.models import BaseDocument

class ChatbotTypes(StrEnum):
    rag="RAG"
    agent="AGENT"
    chatbot="CHATBOT"
    writing_bot="WRITING-BOT"
    assistant="ASSISTANT"
    
class ChatbotStatus(StrEnum):
    ready="READY"
    init="INIT"

class Metadata(EmbeddedDocument):
    is_voice = BooleanField(default=False)
    is_private = BooleanField(default=False)
    is_deleted = BooleanField(default=False)
    is_archived = BooleanField(default=False)
    is_favorite = BooleanField(default=False)

class DBChatbot(BaseDocument):
    name = StringField()
    ownerId = StringField()
    knowledgeBases = ListField(ReferenceField)
    type = EnumField(ChatbotTypes)
    status = EnumField(ChatbotStatus)
    metadata = EmbeddedDocumentField(Metadata)

    meta = {'collection': 'chatbot'}