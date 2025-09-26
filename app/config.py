import os
from dotenv import load_dotenv
from neomodel import config

load_dotenv()

class Settings:
    NEO4J_AURA_URI = os.getenv("NEO4J_AURA_URI", "")
    NEO4J_AURA_USERNAME = os.getenv("NEO4J_AURA_USERNAME", "")
    NEO4J_AURA_PASSWORD = os.getenv("NEO4J_AURA_PASSWORD", "")
    NEO4J_AURA_DATABASE = os.getenv("NEO4J_AURA_DATABASE", "neo4j")

settings = Settings()

# Debug output
print("=== Neo4j Configuration ===")
print(f"URI: {settings.NEO4J_AURA_URI}")
print(f"Username: {settings.NEO4J_AURA_USERNAME}")
print(f"Password: {'*' * len(settings.NEO4J_AURA_PASSWORD) if settings.NEO4J_AURA_PASSWORD else 'None'}")

# Configure neomodel for Aura
if all([settings.NEO4J_AURA_URI, settings.NEO4J_AURA_USERNAME, settings.NEO4J_AURA_PASSWORD]):
    # For Aura, use the direct neo4j+s URL format
    aura_uri = settings.NEO4J_AURA_URI.replace('neo4j+s://', '')
    config.DATABASE_URL = f"neo4j+s://{settings.NEO4J_AURA_USERNAME}:{settings.NEO4J_AURA_PASSWORD}@{aura_uri}"
    config.ENCRYPTED = True
    config.MAX_CONNECTION_POOL_SIZE = 10
    
    print("✅ Neo4j Aura configuration loaded")
    print(f"Database URL: neo4j+s://{settings.NEO4J_AURA_USERNAME}:{'*' * len(settings.NEO4J_AURA_PASSWORD)}@{aura_uri}")
    
    # Test connection
    try:
        from neomodel import db
        result, meta = db.cypher_query("RETURN 'Connection test' AS message")
        print("✅ Database connection test successful!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
else:
    print("❌ Missing Neo4j configuration")
    # Fallback to prevent app crash
    config.DATABASE_URL = "bolt://localhost:7687"