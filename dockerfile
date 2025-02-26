# Use an official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only essential files for installing dependencies
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run migrations
# ENTRYPOINT ["alembic"]
# CMD ["upgrade", "head"]
