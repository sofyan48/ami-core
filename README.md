# MANAGE YOUR SERVERS

## Requirements OS
```
apt install ansible python-pip libmysqlclient-dev
pip install mysql-python
```

## Requirements Apps
```
apt install python3 python3-pip python3-dev
pip install -e .
```

# RUN APP
## configure ami playbooks
```
cd docs
ami playbook configure
sudo ami playbook start
```
