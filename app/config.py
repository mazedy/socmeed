import os
from dotenv import load_dotenv
from neomodel import config

# Load .env from current working directory (where you run uvicorn from)
load_dotenv()

print("=== Loading environment variables ===")

class Settings:
    NEO4J_AURA_URI = os.getenv("NEO4J_AURA_URI")
    NEO4J_AURA_USERNAME = os.getenv("NEO4J_AURA_USERNAME")
    NEO4J_AURA_PASSWORD = os.getenv("NEO4J_AURA_PASSWORD")
    NEO4J_AURA_DATABASE = os.getenv("NEO4J_AURA_DATABASE", "neo4j")

settings = Settings()

# Debug output
print(f"URI: {settings.NEO4J_AURA_URI}")
print(f"Username: {settings.NEO4J_AURA_USERNAME}")
print(f"Password: {'*' * len(settings.NEO4J_AURA_PASSWORD) if settings.NEO4J_AURA_PASSWORD else 'None'}")

if settings.NEO4J_AURA_URI and settings.NEO4J_AURA_USERNAME and settings.NEO4J_AURA_PASSWORD:
    uri_clean = settings.NEO4J_AURA_URI.replace('neo4j+s://', '')
    config.DATABASE_URL = f"bolt+s://{settings.NEO4J_AURA_USERNAME}:{settings.NEO4J_AURA_PASSWORD}@{uri_clean}"
    config.ENCRYPTED = True
    print("✅ Neo4j configured successfully!")
else:
    config.DATABASE_URL = "bolt://localhost:7687"
    print("❌ Missing Neo4j configuration")