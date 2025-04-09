# Use an official Python runtime
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy the local files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

# Run the app
CMD ["python", "serve_model.py"]
