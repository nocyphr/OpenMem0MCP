FROM python:3.11-slim

WORKDIR /app
RUN pip install "mcp[cli]"

EXPOSE 8000
CMD ["python", "src/server.py"]
