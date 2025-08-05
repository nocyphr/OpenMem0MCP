from mem0 import Memory
from mem0.configs.base import MemoryConfig

# Method 1: Using MemoryConfig object
config = MemoryConfig(
    embedder={
        "provider": "litellm",
        "config": {
            "model": "text-embedding-3-small",
            "api_key": "your-api-key"
        }
    }
)
memory = Memory(config=config)

# Method 2: Let Memory create the config
memory = Memory(
    embedder={
        "provider": "litellm", 
        "config": {
            "model": "text-embedding-3-small",
            "api_key": "your-api-key"
        }
    }
)
