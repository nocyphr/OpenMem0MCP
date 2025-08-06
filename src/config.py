from mem0.configs.base import MemoryConfig
import os
from prompts import inputthought

vconfig = {
    "provider": os.getenv('VECTORSTORE_PROVIDER'),
    "config": {
        "url": os.getenv('VECTORSTORE_URL'),
        "collection_name": os.getenv('VECTORSTORE_COLLECTION_NAME'),
        "embedding_model_dims": os.getenv('EMBEDDING_DIMS'),
    },
}


embedconfig = {
    "provider": os.getenv('EMBEDDING_PROVIDER'),
    "config": {
        "api_key": os.getenv("EMBEDDING_PROVIDER_API_KEY"),
        "model": os.getenv('EMBEDDING_MODEL'),
        "embedding_dims": os.getenv('EMBEDDING_DIMS'),
    },
}

llmconfig = {
    "provider": os.getenv('GENERAL_LLM_PROVIDER'),
    "config": {
        "model": os.getenv('GENERAL_LLM_MODEL'),
        "temperature": os.getenv('GENERAL_LLM_TEMP'),
        "max_tokens": os.getenv('GENERAL_LLM_MAX_TOKEN')},
}

graphconfig = {
    "provider": os.getenv('GRAPH_TYPE'),
    "config": {
        "url": os.getenv('GRAPH_URL'),
        "username": os.getenv("NEO4J_USER"),
        "password": os.getenv("NEO4J_PASSWORD"),
        "database": os.getenv('GRAPH_TYPE')
    },
    "llm": {
        "provider": os.getenv('GRAPH_LLM_PROVIDER'),
        "config": {
            'model': os.getenv('GRAPH_LLM_MODEL'),
            "temperature": os.getenv('GRAPH_LLM_TEMP'),
            "max_tokens": os.getenv('GRAPH_LLM_MAX_TOKEN'),
        },
    },
    # "custom_prompt": ...,
}
fact_extraction_prompt: str = f"""
Extract the relevant facts and information from the content in a json format as shown below

Input: My order #12345 hasn't arrived yet.
Output: {{"facts" : ["Order #12345 not received"]}}

Input: {inputthought}
Output: {{
  "facts": [
    "Evolving systems are more effective than perfection.",
    "Actions today influence whether tomorrow is easier or harder.",
    "Quotes are powerful due to their distilled, singular format.",
    "Women's self-esteem may be boosted at the cost of limiting male potential in relationships.",
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
