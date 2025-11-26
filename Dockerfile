# Use a lightweight Python image
FROM python:3.11-slim

# Create directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port Render expects
EXPOSE 10000

# Start the server
CMD ["python", "app.py"]
