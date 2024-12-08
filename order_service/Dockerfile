# Use official Python image from Docker Hub
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5002


# Run the app
CMD ["python", "app.py"]
