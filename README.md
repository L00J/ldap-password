# ldap-password

#### 介绍
自助修改ldap用户密码

#### 环境
![Python](https://img.shields.io/badge/python-3.7-blue.svg?style=plastic)
![django](https://img.shields.io/badge/django-3.0.5-blue.svg?style=plastic)
![bootstrap](https://img.shields.io/badge/bootstrap-3.3.7-green.svg?style=plastic)
![python-ldap](https://img.shields.io/badge/python_ldap-3.2.0-red.svg?style=plastic)

#### 安装教程
**Docker快速部署**
```
docker  run -d -p 8000:8080  --env LDAP_HOST="192.168.1.250"  --env LDAP_ADMIN_USER="root.ops.net"  --env LDAP_PASSWORD="PASSWD"    lghost/ldap-password:latest
# LDAP_HOST是ldap服务器地址； LDAP_ADMIN_USER是manager账号; LDAP_PASSWORD是manager密码
```

**调试打印输出**
`docker   -it  -p 8000:8080  -rm  ...省略` 

Django version 3.0.5, using settings 'website.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
[10/Apr/2020 00:09:49] "GET / HTTP/1.1" 200 4824
LDAP connect success!
[10/Apr/2020 00:09:58] "POST / HTTP/1.1" 200 18
LDAP connect success!
user: test modify passwd success

####
```

git clone https://gitee.com/attacker/ldap-password.git
ip install -i http://mirrors.aliyun.com/pypi/simple   --trusted-host mirrors.aliyun.com requirements.txt
python manage.py runserver 0.0.0.0:80
```

#### 使用说明


<!--![首页](doc/home.jpeg)-->

<img src="http://attacker.gitee.io/ldap-password/home.jpeg" width="80%">