# Use official Python image
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy the .env file
COPY .env .env

# Copy all files to container
COPY . .



# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn  # No need for Streamlit in Flask API container

# Expose Flask API port
EXPOSE 5000

# Default command for running Flask API with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
