# Base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY .. .

# Expose the port on which the Flask server will run
EXPOSE 5000

# Set the entry point command to run the Flask server
CMD ["python", "app.py"]
