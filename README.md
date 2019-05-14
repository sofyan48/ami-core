# MANAGE YOUR SERVERS

## Requirements OS
```
apt install ansible python-pip libmysqlclient-dev
pip install python-mysql
```

## Requirements core
```
apt install python3 python3-pip python3-dev
pip3 install pymysql

pip install -e .
```

# RUN APP
## configure ami playbooks
```
cd docs
ami playbook configure
sudo ami playbook start
```
