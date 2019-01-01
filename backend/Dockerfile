# Build step

FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "flask", "run", "-h", "0.0.0.0" ]
EXPOSE 5000