FROM python:3.8-buster

COPY . .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --user -r requirements.txt

CMD [ "python3", "-u", "./app.py" ]