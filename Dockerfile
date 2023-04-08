FROM python:3.9.1
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /The-Fun-Bot
WORKDIR /The-Fun-Bot
COPY . .
CMD ["/bin/bash", "/start.sh"]
