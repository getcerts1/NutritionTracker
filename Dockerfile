FROM python:3.13-alpine


# Set working directory
WORKDIR /opt/app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Run the application
CMD ["python3", "main.py"]

