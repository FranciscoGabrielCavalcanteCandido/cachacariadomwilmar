FROM python:3.12.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install crispy-bootstrap5 && pip install django-crispy-forms
    
COPY . /code/   
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "cachacariadomwilmar.wsgi:application"]   
