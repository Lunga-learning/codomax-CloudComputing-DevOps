FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from creating unnecessary cache files
ENV PYTHONDONTWRITEBYTECODE=1

# Display Python logs immediately
ENV PYTHONUNBUFFERED=1

# Install application dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application into the container
COPY . .

# Expose Flask application port
EXPOSE 5000

# Start Flask using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "run:app"]
