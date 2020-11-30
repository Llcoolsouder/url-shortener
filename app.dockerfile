FROM python:3.8

COPY backend/ ./backend/
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

WORKDIR /backend/

ENTRYPOINT [ "gunicorn" ]
CMD [ "-b 0.0.0.0:5000", "app:app" ]