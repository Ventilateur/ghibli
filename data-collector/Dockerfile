FROM python:3.8-buster

COPY . .

# install dependencies to the local user directory (eg. /root/.local)
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --user -r requirements.txt

CMD [ "python3", "-u", "./app.py" ]