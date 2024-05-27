FROM python:3.11-alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY app ./app
COPY main.py ./
COPY settings.py ./

CMD ["fastapi", "run", "main.py", "--port", "8000"]