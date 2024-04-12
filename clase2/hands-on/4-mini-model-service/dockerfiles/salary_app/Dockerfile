FROM python:3.10-slim

WORKDIR /app

# Install python requirements
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# Copy App
COPY /app .

# Expose streamlit port
EXPOSE 8501

# Run the command on container startup
ENTRYPOINT ["streamlit", "run", "./app.py"]
