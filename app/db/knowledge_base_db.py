from typing import List

from app.db import convert_inbound_factory, convert_outbound_factory
from app.models.knowledge_base_models import DBKnowledgeBase
from app.schema.knowledge_base_schema import KnowledgeBaseIn

convert_inbound = convert_inbound_factory("knowledge_base_id")
convert_outbound = convert_outbound_factory("knowledge_base_id")

async def get_knowledge_base_by_id(knowledge_base_id: str) -> DBKnowledgeBase:
    db_knowledge_base = await DBKnowledgeBase.objects(id=knowledge_base_id).first()
    return convert_inbound(db_knowledge_base)

async def get_all_knowledge_bases_by_owner(owner_id: str) -> List[DBKnowledgeBase]:
    db_knowledge_bases = await DBKnowledgeBase.objects(owner_id=owner_id)
    return [convert_inbound(db_knowledge_base) for db_knowledge_base in db_knowledge_bases]

async def save_knowledge_base(knowledge_base: KnowledgeBaseIn) -> DBKnowledgeBase:
    db_knowledge_base = DBKnowledgeBase(**convert_outbound(knowledge_base))
    db_knowledge_base.save()
    return convert_inbound(db_knowledge_base)

async def update_knowledge_base(knowledge_base: KnowledgeBaseIn) -> DBKnowledgeBase:
    db_knowledge_base = await DBKnowledgeBase.objects(id=knowledge_base.knowledge_base_id).first()
    db_knowledge_base.update(**convert_outbound(knowledge_base))
    return convert_inbound(db_knowledge_base)

async def delete_knowledge_base(knowledge_base_id: str) -> DBKnowledgeBase: 
    db_knowledge_base = await DBKnowledgeBase.objects(id=knowledge_base_id).first()
    db_knowledge_base.delete()
    return convert_inbound(db_knowledge_base)