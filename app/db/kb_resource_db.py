from app.db import convert_inbound_factory, convert_outbound_factory
from app.models.knowledge_base_models import DBKbResource
from app.schema.kb_resource_schema import KBResourceIn

convert_inbound = convert_inbound_factory("kb_resource_id")
convert_outbound = convert_outbound_factory("kb_resource_id")

async def save_kb_resource(kb_resource: KBResourceIn) -> DBKbResource:
    db_kb_resource = DBKbResource(**convert_outbound(kb_resource))
    db_kb_resource.save()
    return convert_inbound(db_kb_resource)