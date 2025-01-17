from mongoengine import connect, disconnect
import logging
from app.common import utils_service

from app.config import settings

logger = logging.getLogger(__name__)

def init_db():
    """Initialize database connection"""
    logger.info(f"Connecting to MongoDB at {settings.MONGODB_URL}")
    connect(
        db=settings.MONGODB_DB_NAME,
        host=settings.MONGODB_URL,
        alias="default"
    )
    logger.info("Successfully connected to MongoDB")

def close_db():
    """Close database connection"""
    logger.info("Closing MongoDB connection")
    disconnect(alias="default")
    logger.info("MongoDB connection closed")

def convert_inbound_factory(id_name):  # mongo to core.
    def convert_inbound(data):
        if data is None:
            return data
        data_inbound = utils_service.convert_dict_c2s(
            data.to_mongo().to_dict())
        if '_id' in data_inbound:
            data_inbound[id_name] = str(data_inbound.pop("_id"))
        return data_inbound
    return convert_inbound

def convert_outbound_factory(id_name):  # mongo to core.
    def convert_outbound(data: dict):
        outbound_data = dict(data)
        if outbound_data is None:
            return outbound_data
        if id_name in outbound_data:
            outbound_data["id"] = str(outbound_data.pop(id_name))
        return utils_service.convert_dict_s2c(outbound_data)
    return convert_outbound
