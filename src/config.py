from mem0.configs.base import MemoryConfig
import os
from prompts import inputthought

vconfig = {
    "provider": "milvus",
    "config": {
        "url": "http://milvus:19530",
        "collection_name": "personal_memories",
        "embedding_model_dims": 2048,
    },
}


embedconfig = {
    "provider": "litellm",
    "config": {
        "api_key": os.getenv("VOYAGEAI_API_KEY"),
        "model": "voyage/voyage-3-large",
        "embedding_dims": 2048,
    },
}

llmconfig = {
    "provider": "litellm",
    "config": {"model": "gpt-4o", "temperature": 0.7, "max_tokens": 10000},
}

graphconfig = {
    "provider": "neo4j",
    "config": {
        "url": "bolt://neo4j:7687",
        "username": os.getenv("NEO4J_USER"),
        "password": os.getenv("NEO4J_PASSWORD"),
        "database": "neo4j",
    },
    "llm": {
        "provider": "litellm",
        "config": {
            'model': 'claude-3-7-sonnet-20250219',
            # "model": "claude-sonnet-4-20250514",
            "temperature": 0.7,
            "max_tokens": 64000,
        },
    },
    # "custom_prompt": ...,
}
print(graphconfig, flush=True)
fact_extraction_prompt: str = f"""
Extract the relevant facts and information from the content in a json format as shown below

Input: My order #12345 hasn't arrived yet.
Output: {{"facts" : ["Order #12345 not received"]}}

Input: {inputthought}
Output: {{
  "facts": [
    "Evolving systems are more effective than perfection.",
    "Actions today influence whether tomorrow is easier or harder.",
    "Men often achieve peak accomplishments with supportive women, not because of them.",
    "Women's self-esteem may be boosted at the cost of limiting male potential in relationships.",
    "Quotes are powerful due to their distilled, singular format.",
    "Life quality suffers when dependent on an unreliable person.",
    "Trying to prevent an idiot from making mistakes may result in becoming one.",
    "Repeated pain that didn’t teach will likely not be outdone by advice.",
    "When external noise ceases, the mind seeks a new source.",
    "Self-agency persists despite circumstances.",
    "A job is transient like water; skills are the constant source.",
    "You owe decency, primarily to yourself."
  ]
}}


If information is present, state it directly and concisely, with no introductory wording.
If markdown is a tutorial/instruction make sure you do not remove any information or change the sequence!
If you find something that sounds like it could be a quote, ensure its unchanged integrity. 
If you find code, make sure you ensure its unchanged integrity
a chain of thought should become an ordered list

Content:
"""

memory_config = MemoryConfig(
    vector_store=vconfig,
    embedder=embedconfig,
    llm=llmconfig,
    version="v2",
    graph_store=graphconfig,
    history_db_path=os.getenv('DB_URL'),
    custom_fact_extraction_prompt=fact_extraction_prompt,
)
