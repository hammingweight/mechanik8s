FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Create /hostcgroups directory in root
RUN mkdir -p /hostcgroups

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app .

# Set entrypoint
ENTRYPOINT ["python", "main.py"]