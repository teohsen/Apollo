FROM python:3.11-slim-bullseye

WORKDIR /app
COPY . /app

RUN pip install poetry==1.6.1
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "bookmark.py"]