FROM python:3.13-slim

# Working directory
WORKDIR /app

# Make /app available for Python imports
ENV PYTHONPATH=/app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Run tests
CMD ["python", "-m", "pytest", "-v"]