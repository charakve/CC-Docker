# Stage 1: Builder (includes build dependencies)
FROM python:3.9-alpine AS build

# Install build dependencies needed for Python packages
RUN apk add --no-cache gcc musl-dev libffi-dev

# Set working directory
WORKDIR /home/data

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Stage (no build dependencies)
FROM python:3.9-alpine

# Set working directory
WORKDIR /home/data

# Copy only necessary files from the build stage
COPY --from=build /usr/local/lib/python3.9/ /usr/local/lib/python3.9/
COPY --from=build /usr/local/bin/ /usr/local/bin/

# Copy project files
COPY . /home/data

# Run the Python script
CMD ["python", "/home/data/scripts.py"]
