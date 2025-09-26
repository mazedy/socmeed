from neomodel import (
    StructuredNode,
    StringProperty,
    DateTimeProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
    EmailProperty
)
from datetime import datetime

class User(StructuredNode):
    uid = UniqueIdProperty()
    username = StringProperty(unique_index=True, required=True)
    email = EmailProperty(unique_index=True, required=True)
    created_at = DateTimeProperty(default=datetime.utcnow)
    updated_at = DateTimeProperty(default=datetime.utcnow)
    
    # Relationships
    posts = RelationshipTo('Post', 'CREATED')
    friends = RelationshipTo('User', 'FRIENDS_WITH')
    likes = RelationshipTo('Post', 'LIKES')
    following = RelationshipTo('User', 'FOLLOWS')
    followers = RelationshipFrom('User', 'FOLLOWS')  # Reverse relationship

class Post(StructuredNode):
    uid = UniqueIdProperty()
    content = StringProperty(required=True)
    created_at = DateTimeProperty(default=datetime.utcnow)
    updated_at = DateTimeProperty(default=datetime.utcnow)
    
    # Relationships
    author = RelationshipFrom('User', 'CREATED')
    likes = RelationshipFrom('User', 'LIKES')