# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Expose Gradio port
EXPOSE 7860

# Run Gradio app
CMD ["python", "app_gradio.py"]
