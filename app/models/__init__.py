from datetime import datetime
from mongoengine import Document, DateTimeField

class BaseDocument(Document):
    meta = {'abstract': True}  # This makes it an abstract base class
    
    createdAt = DateTimeField(default=datetime.utcnow)
    modifiedAt = DateTimeField(default=datetime.utcnow)
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.utcnow()
        self.modified_at = datetime.utcnow()
        return super().save(*args, **kwargs)