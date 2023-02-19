FROM python:3.7

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

ENV PYTHONPATH=/app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["app.api:app", "--host", "0.0.0.0"]