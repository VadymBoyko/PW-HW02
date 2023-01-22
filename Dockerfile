FROM python:3.10

WORKDIR /app

COPY . .

CMD ["poetry", "run", "python", "main.py"]