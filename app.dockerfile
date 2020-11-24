FROM python:3.8

COPY app.py .
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "flask" ]
CMD [ "run", "--host=0.0.0.0", "--port=5000"]