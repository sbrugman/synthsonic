FROM tiangolo/uvicorn-gunicorn:python3.7

ENV PYTHONPATH /app

COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app/api/

EXPOSE 8000

CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8000"]