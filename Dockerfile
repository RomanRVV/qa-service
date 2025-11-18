FROM docker.io/python:3.10

ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

ENV BASE_DIR=/opt/app
WORKDIR ${BASE_DIR}


RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ${BASE_DIR}/
RUN pip install --no-cache-dir -r requirements.txt

COPY . ${BASE_DIR}/

ENV PYTHONPATH="${PYTHONPATH}:${BASE_DIR}/src"

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=webapp.settings \
    DJANGO__DEBUG=true \
    DJANGO__SECRET_KEY=test_key \
    DATABASE=postgresql://myuser:mypassword@db:5432/myproject

WORKDIR ${BASE_DIR}/src

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
