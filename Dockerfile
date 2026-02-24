FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN addgroup --system commagroup && adduser --system --ingroup commagroup comma
USER comma

EXPOSE 8080

ENTRYPOINT ["python", "main.py"]
