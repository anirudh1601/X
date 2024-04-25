FROM python:3.12

ENV PYTHONBUFFERED=1

WORKDIR /dock

COPY req.txt .

RUN pip install -r req.txt

COPY . .

EXPOSE 8000

CMD ['cd ']
CMD ["python", "manage.py", "runserver","0.0.0.0:7000"]

