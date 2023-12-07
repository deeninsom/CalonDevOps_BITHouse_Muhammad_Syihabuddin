FROM python:3.10.12

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libdbus-1-dev \
    libcups2-dev \
    libgirepository1.0-dev 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code

COPY requirements.txt /code

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /code/requirements.txt && \
    rm -rf /root/.cache/

COPY . /code/

# RUN python manage.py makemigrations && python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
