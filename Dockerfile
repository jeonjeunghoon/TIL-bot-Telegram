FROM ubuntu:latest
MAINTAINER jeonjeunghoon

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install datetime --upgrade
RUN pip3 install beautifulsoup4 --upgrade
RUN pip3 install requests --upgrade
RUN pip3 install datetime --upgrade
RUN pip3 install python-telegram-bot --upgrade
RUN pip3 install schedule --upgrade

RUN mkdir app/

WORKDIR /app

ADD ./app

EXPOSE 80

CMD []