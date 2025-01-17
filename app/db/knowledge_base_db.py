from app.db import convert_inbound_factory, convert_outbound_factory
from app.models.knowledge_base_models import DBKnowledgeBase
from app.schema.knowledge_base_schema import KnowledgeBaseIn

convert_inbound = convert_inbound_factory("knowledge_base_id")
convert_outbound = convert_outbound_factory("knowledge_base_id")

async def save_knowledge_base(knowledge_base: KnowledgeBaseIn) -> DBKnowledgeBase:
    db_knowledge_base = DBKnowledgeBase(**convert_outbound(knowledge_base))
    db_knowledge_base.save()
    return convert_inbound(db_knowledge_base)
