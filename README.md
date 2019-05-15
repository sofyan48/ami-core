# MANAGE YOUR SERVERS AND INSTALL SERVER PACKAGE


# INSTALLING

## Requirements OS
Ubuntu Based
```
apt install ansible python-pip libmysqlclient-dev gcc
pip install mysql-python
```

Centos Based
```
yum install epel-release
yum install ansible python2-pip mariadb-devel gcc
pip install mysql-python
```

## Requirements Apps

Debian Based
```
apt install python3 python3-pip python3-dev
pip3 install -e .
```

Centos Based
```
yum install python36 python36-pip python36-dev
pip3 install -e .
```

# RUNNING APP EXAMPLE
To see more examples, open the docs folder

## configure ami playbooks

Make a file with the name ami.yml
```
yum:
  hosts: all
  roles:
    - commons
    - mariadb
    - nginx
    - php
    - wordpress
  vars:
    mariadb:
      password: password
    wordpress:
      db_name: testing
      username: iank
      password: qwerty123
      wp_url: "103.93.53.31"
      email: meongbego@gmail.com
```
run playbook configure | wait report in playbook configured
```
$ ami playbook configure
2019-05-16 04:50:34 localhost.localdomain root[30300] INFO Playbook Configured
```
After this report now execute 
```
$ ami playbook start
2019-05-16 04:50:34 localhost.localdomain root[30300] INFO Package Finished
```

Note : This Project under development
