FROM python:3.11-slim
RUN pip install --no-cache-dir uv
WORKDIR /app
COPY . /app
RUN uv pip install --system .
CMD ["casual-mcp-server-words"]
