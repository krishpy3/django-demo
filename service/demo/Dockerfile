# Be sure to copy .env.example over to .env and fill it in.
#
# Basic commands to build & run the container:
#   docker build -t sciam_django:latest .
#   docker run --rm -p 8000:8000 sciam_django:latest

FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

EXPOSE 8000

RUN python manage.py migrate
RUN python manage.py collectstatic
RUN . ./.env && python manage.py createsuperuser --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-w", "4", "project.wsgi"]
