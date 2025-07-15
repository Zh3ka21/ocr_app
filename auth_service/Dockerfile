# Use Python 3.12 slim
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Python
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

# Set the working directory inside the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Configure Poetry to install dependencies globally
RUN poetry config virtualenvs.create false

# Copy dependency files first (cache optimization)
COPY pyproject.toml poetry.lock ./

# Install dependencies (no virtualenv)
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the application code
COPY src/ ./src

# Copy the entrypoint script and make sure it is executable
COPY start_server.sh .
RUN chmod +x start_server.sh

# Set environment for module resolution
ENV PYTHONPATH=/app/src

# Expose port
EXPOSE 8000

# Entrypoint
ENTRYPOINT ["./start_server.sh"]
