FROM python:3.8

COPY app.py .
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "flask" ]
CMD [ "run", "--host=0.0.0.0", "--port=5000"]