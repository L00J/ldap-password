FROM python:3.7-alpine
MAINTAINER  by LJ <admin@attacker.club>

WORKDIR /home
COPY . /home
RUN  sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories  &&apk add libldap gcc libc-dev python-dev openldap-dev
RUN pip  install -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com  -r  requirements.txt
RUN apk del gcc libc-dev python-dev openldap-dev

#  RUN  python manage.py makemigrations  &&  python manage.py migrate
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8080"]
#CMD [ "/home/run"]


# docker build -t lghost/ldap-password:latest . # build images
#