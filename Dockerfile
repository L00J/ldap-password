
FROM python:3.8-alpine

WORKDIR /home
COPY . /home
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && apk add libldap gcc libc-dev python-dev openldap-dev
RUN pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r requirements.txt
RUN apk del gcc libc-dev python-dev openldap-dev 
RUN  rm -rf /home/env && rm -f /var/cache/apk/*

#  RUN  python manage.py makemigrations  &&  python manage.py migrate
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]


# docker build -t lghost/ldap-password:latest . # build images
# docker push lghost/ldap-password:latest # 推送到dockerhub
# RUN: docker  run --restart=always -d -p 8000:8000  --env LDAP_HOST="192.168.1.250"  --env LDAP_ADMIN_USER="root.ops.net"  --env LDAP_PASSWORD="PASSWD" --name ldap-password lghost/ldap-password:latest
