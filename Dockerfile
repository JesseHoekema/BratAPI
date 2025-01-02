FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app/

# Install system dependencies and create a virtual environment
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    && python -m venv /opt/venv && \
    /bin/bash -c "source /opt/venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt" && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH"

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
