FROM python:3.8-buster

RUN python3 -m pip install --upgrade pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install --user -r requirements.txt

COPY . /app

CMD [ "python3", "-u", "./app.py" ]