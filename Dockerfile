# Use a Debian-based Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libjpeg-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python -m pip install --upgrade pip

# Copy the requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app/

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["python", "main.py"]
