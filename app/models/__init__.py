from datetime import datetime
from mongoengine import Document, DateTimeField

class BaseDocument(Document):
    meta = {'abstract': True}  # This makes it an abstract base class
    
    createdAt = DateTimeField(default=datetime.utcnow)
    modifiedAt = DateTimeField(default=datetime.utcnow)
    
    def save(self, *args, **kwargs):
        if not self.createdAt:
            self.created_at = datetime.utcnow()
        self.modifiedAt = datetime.utcnow()
        return super().save(*args, **kwargs)