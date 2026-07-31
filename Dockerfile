FROM python:3.11-slim

WORKDIR /app

# System deps for PyQt5 (headless)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libegl1-mesa \
    libxcb-cursor0 \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

COPY . .

ENTRYPOINT ["python", "-m", "eva"]
