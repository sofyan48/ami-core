import yaml
import os
import subprocess
import coloredlogs
import logging
import psutil
import shutil
import hashlib
import uuid
import fileinput
import requests
from ami import __appname__
from dotenv import load_dotenv
import git


app_root = os.path.dirname(os.path.abspath(__file__))
app_home = os.path.expanduser("~")
app_cwd =  os.getcwd()
config_folder = app_home+"/.config/"+__appname__+"/"

def question(word):
    answer = False
    while answer not in ["y", "n"]:
        answer = input("{} [y/n]? ".format(word)).lower().strip()

    if answer == "y":
        answer = True
    else:
        answer = False
    return answer

def log_rep(stdin):
    coloredlogs.install()
    logging.info(stdin)

def log_warn(stdin):
    coloredlogs.install()
    logging.warn(stdin)

def log_err(stdin):
    coloredlogs.install()
    logging.error(stdin)

def template_git(url, dir):
    try:
        chk_repo = os.path.isdir(dir)
        if chk_repo:
            shutil.rmtree(dir)
        git.Repo.clone_from(url, dir)
        return True
    except Exception as e:
        log_err(e)
        return False

def yaml_writeln(stream, path):
    with open(path, '+a') as outfile:
        try:
            yaml.dump(stream, outfile, default_flow_style=False)
        except yaml.YAMLError as exc:
            print(exc)
        else:
            return True

def yaml_read(path):
    with open(path, 'r') as outfile:
        try:
            data = yaml.load(outfile, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)
        else:
            return data

def nvc_repo():
    return yaml_read(app_root+"/templates/repo.yml")

def nvc_config():
    return yaml_read(app_root+"/templates/config.yml")

def nvc_config_roles(pkg):
    return yaml_read(app_root+"/templates/"+pkg+"/roles/item.yml")

def nvc_config_vars(pkg):
    return yaml_read(app_root+"/templates/"+pkg+"/vars/item.yml")

def get_cpu_info():
    cpu = psutil.cpu_times()
    count_cpu = psutil.cpu_count()
    cpu_data = {
        "user": cpu[0],
        "nice": cpu[1],
        "system": cpu[2],
        "idle": cpu[3],
        "count": count_cpu,
    }
    return cpu_data

def get_memory_info():
    memory = psutil.virtual_memory()
    swap = psutil.virtual_memory()
    mem_data = {
        "physmem":{
            "total": memory[0],
            "available": memory[1],
            "percent": memory[2],
            "used": memory[3],
            "free": memory[4]
        },
        "swap":{
          "total": swap[0],
            "available": swap[1],
            "percent": swap[2],
            "used": swap[3],
            "free": swap[4]
        }
    }
    return mem_data

def get_disk_info():
    disk = psutil.disk_usage('/')
    disk_data = {
        "total": disk[0],
        "used": disk[1],
        "free": disk[2],
        "percent": disk[3]
    }
    return disk_data


def create_file(file, path, value=None):
    default_path = config_folder
    if path:
        default_path = str(path)
    f=open(default_path+"/"+file, "a+")
    f.write(value)
    f.close()

    try:
        return read_file(default_path+"/"+file)
    except Exception as e:
        print(e)

def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def check_folder(path):
    return os.path.isdir(path)

def copyfile(src, dest):
    try:
        shutil.copyfile(src, dest)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def create_folder(path):
    return os.makedirs(path)

def read_file(file):
    if os.path.isfile(file):
        return True
    else:
        return False

def rm_dir(path):
    return shutil.rmtree(path)

def token_hash(string):
    random_string = uuid.uuid4()
    raw_token = '{}{}'.format(random_string, string)
    access_token = hashlib.sha256(raw_token.encode(
        'utf-8')).hexdigest()
    return access_token

def get_http(url, headers=None):
    send = requests.get(url, headers=headers)
    respons = send.json()
    return respons

def send_http(url, data = None, headers=None):
    send = requests.post(url, json=data, headers=headers)
    respons = send.json()
    return respons

def load_env_file():
    return load_dotenv(config_folder+"ami.env", override=True)

def check_env():
    return os.path.isfile(config_folder+"ami.env")

def check_env_default():
    return os.path.isfile(config_folder+"default.env")

def get_env_values():
    if check_env():
        load_env_file()
        ami_env = {}
        ami_env['token'] = os.environ.get('OS_TOKEN')
        ami_env['project_id'] = os.environ.get('OS_PROJECT_ID')
        return ami_env
    else:
        print("Can't find ami.env")

def create_env_file(token, project_id = None):
    if check_env():
        os.remove(config_folder+"ami.env")
    try:
        env_file = open(config_folder+"ami.env", "w+")
        env_file.write("OS_TOKEN=%s\n" % token)
        env_file.write("OS_PROJECT_ID=%s\n" % project_id)
        env_file.close()
        return True
    except Exception as e:
        print(e)
        return False

def create_env_default(url, port):
    if not os.path.isdir(config_folder):
        create_folder(config_folder)
    try:
        env_file = open(config_folder+"default.env", "w+")
        env_file.write("OS_URL=%s\n" % url)
        env_file.write("OS_PORT=%s\n" % port)
        env_file.close()
        return True
    except Exception as e:
        print(e)
        return False

def get_env_default():
    if check_env():
        load_dotenv(config_folder+"default.env", override=True)
        def_ami_env = {}
        def_ami_env['url'] = os.environ.get('OS_URL')
        def_ami_env['port'] = os.environ.get('OS_PORT')
        def_ami_env['proxy'] = os.environ.get('OS_PROXY')
        def_ami_env['proxy_file'] = os.environ.get('OS_PROXY_FILE')
        return def_ami_env
    else:
        print("Can't find ami default.env")

def setting_repo():
    return yaml_read(app_root+"/templates/setting.yml")

def restart_proxy():
    os.system("systemctl restart haproxy")

def replace_text(file, search, replace):
    with fileinput.FileInput(file, inplace=True, backup='.ami') as file:
        for line in file:
            print(line.replace(search, replace), end='')