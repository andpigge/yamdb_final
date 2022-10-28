FROM python:3.7-slim

LABEL email="rustamaaaa@bk.ru"

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["sh", "start.sh"]
