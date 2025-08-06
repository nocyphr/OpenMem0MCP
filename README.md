# OpenMem0MCP

**OpenMem0MCP** is a fast, pluggable memory control server that wraps the [`mem0`](https://pypi.org/project/mem0ai/) Python package and exposes a simple HTTP interface for long-term memory operations: **memorize** (add) and **remember** (search).

This project is designed to be modular, production-ready, and highly configurable, enabling you to swap out the memory backend, vector store, embedding provider, and graph store — all through environment variables.

This package includes two companion patches that make the mem0 Python SDK suitable for real-world, concurrent, production environments.

## What This Is

- A Memory Control Protocol (MCP) server exposing `/add` and `/search` endpoints.
- Wraps `mem0` with extended backend support.
- Includes containerized support for:
  - PostgreSQL for relational memory storage.
  - Milvus for high-performance vector similarity search.
  - Neo4j for optional graph-based memory linkage.
- Supports concurrent writes, unlike SQLite.
- Flexible embedding model support beyond what mem0 supports natively.

## Key Enhancements Over mem0

### Patch #1 – SQLAlchemy Backend Expansion
[mem0_history_db_patch](https://pypi.org/project/mem0-history-db-patch/)
- Extends mem0 to support any SQLAlchemy-compatible database.
- Enables PostgreSQL as a robust alternative to SQLite for concurrent environments.
- Included via a pip-installable companion patch.

### Patch #2 – Expanded Embedding Provider Support
[mem0_embeddings_litellm_patch](https://pypi.org/project/mem0-embeddings-litellm-patch/)
- Integrates `litellm` as an embedding backend for mem0.
- Enables support for a wider range of embedding providers and models.
- Offers an easy switch between providers like OpenAI, HuggingFace, and others.

Together, these patches make the original mem0 project suitable for production usage in multi-agent or high-load environments.

## Setup Instructions

### 1. Clone & Configure

```bash
git clone https://github.com/nocyphr/OpenMem0MCP.git
```

Edit `.env` and provide the necessary values:

### 2. Run with Docker Compose

```bash
docker-compose -f docker/docker-compose.yml up --build
```

This launches:

* The MCP server
* Postgres
* Milvus
* Neo4j (optional)

### 3. Test the Endpoints

Use the provided `testme.py` script to verify your setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r docker/requirements.txt
python testme.py
```
Alternatively in `src/client.py` is a sample script that makes an agent use the tools. You can run that too for an agentic test. 
This sends test requests to your running MCP server.

## API Overview

| Endpoint   | Description                      |
| ---------- | -------------------------------- |
| `/memorize`| Add (memorize) new memory        |
| `/recall`  | Query (remember) existing memory |

Note: Deletion and manual updates are not exposed as endpoints. mem0 handles internal consistency and updates automatically when new, conflicting data is added.


## Modular Architecture

You can configure the system to use:

* Any SQLAlchemy-supported database (Supabase/PostgreSQL, MySQL, etc.)
* Any embedding model supported by `litellm`
* Any Graphstore supported by mem0 (default setup is neo4j)
* Any Vectorstore supported by mem0 (default setup is milvus)

All components are swappable through `.env` configuration.

## Usage Note

At this time, the project is designed to run out-of-the-box with:

* MilvusDB (as vector store)
* PostgreSQL (as history database)
* Neo4j (as Graphstore)
If you want to use different databases, graphstores or vector stores, you'll need to either:

* Provide access to an already-hosted instance via environment variable URLs, **or**
* Add the appropriate container and configuration to the existing `docker-compose.yml`.

In the future, additional compose files may be provided for different deployment configurations, but for now, a certain level of manual setup is assumed if you don't want to use the readymade config. 

## Roadmap / To-Do

* [x] Finalize `.env` migration for all config variables
* [ ] Add Traefik reverse proxy
* [ ] add option for raw ingestion to vstore
## Credits

Created and maintained by \[Nocyphr].
Built on top of the excellent [`mem0`](https://pypi.org/project/mem0ai/) project, extended and productionized via custom patches and modular deployment design.

