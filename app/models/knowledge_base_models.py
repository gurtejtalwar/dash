from enum import StrEnum
from mongoengine import (EnumField,
                         IntField,
                         URLField,
                         EmbeddedDocument, 
                         EmbeddedDocumentField, 
                         StringField, ListField, 
                         ReferenceField, CASCADE)

from app.models import BaseDocument

class KnowledgeBaseTypes(StrEnum):
    fast="fast"
    medium="medium"
    accurate="accurate"

class KnowledgeBaseModels(StrEnum):
    openai="openai"
    gemini="gemini"

class KnowledgeBaseStatuses(StrEnum):
    trained="TRAINED"
    ready_to_train="READY-TO-TRAIN"
    error="ERROR"

class KbResourceTypes(StrEnum):
    file="FILE"
    qa="QA"
    url="URL"

class KbResourceStatuses(StrEnum):
    init="INIT"
    read="READY"
    error="ERROR"
    pending_deletion="PENDING_DELETION"
    deleted="DELETED"

class DBContent(EmbeddedDocument):
    fileName = StringField()
    filePath = StringField()
    question = StringField()
    answer = StringField()
    link = URLField()

class DBKnowledgeBase(BaseDocument):
    name=StringField()
    ownerId=StringField()
    type=EnumField(KnowledgeBaseTypes)
    model=EnumField(KnowledgeBaseModels)
    status=EnumField(KnowledgeBaseStatuses)
    tokensUsed=IntField()
    kbResources=ListField(ReferenceField('DBKbResource'))

    meta = {'collection': 'knowledgeBase'}

class DBKbResource(BaseDocument):
    ownerId=StringField()
    type=EnumField(KbResourceTypes)
    status=EnumField(KbResourceStatuses)
    data=StringField()
    knowledgeBase=ReferenceField('DBKnowledgeBase',reverse_delete_rule=CASCADE)
    content=EmbeddedDocumentField(DBContent)
    tokensUsed=IntField()
    meta = {'collection': 'kbResource'}



