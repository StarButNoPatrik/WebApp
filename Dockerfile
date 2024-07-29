# Use the official slim version of Python 3
FROM python:3-slim

# Environment variables to prevent Python from writing pyc files and to ensure output is sent straight to the terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port that Streamlit will run on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app/helloWorld.py"]
