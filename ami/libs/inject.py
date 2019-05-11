from ami.libs import utils
from ami import __appname__
import os

app_home = os.path.expanduser("~")
config_folder = app_home+"/.config/"+__appname__+"/"


def inject_token(data):
    def_env = utils.get_env_default()
    url = def_env['url']
    port = def_env['port']
    url_serial = url+":"+port+"/api/serial"
    respon = utils.send_http(url_serial,data=data)
    if not respon['code'] != "200":
        utils.log_err("Inject Not Successfully")
        return False
    project_id = str(respon['data'][0]['id_serial'])
    url_server = url+":"+port+"/api/server"
    data = {
        "get": {
            "fields": {
                "id_serial": project_id
            }
        }
    }
    check_inject = utils.send_http(url_server, data=data)
    if not check_inject:
        return False
    check_inject = check_inject['data']
    for i in check_inject:
        if i['state']=='1':
            utils.log_err("Inject Already Exist!")
            return False
    token_hash = utils.token_hash(project_id)
    data = {
        "inject": {
            "fields": {
                "token": token_hash,
                "id_serial": str(project_id)
            }
        }
    }
    inject_to_server = utils.send_http(url_server, data=data)
    if not inject_to_server['code'] != "200":
        utils.log_err("Inject Not Successfully")
        return False
    else:
        inject_env = utils.create_env_file(token_hash, project_id)
        if not inject_env:
            return False
    return inject_to_server

def generate_token(project_id):
    question = utils.question("Inject Token")
    if not question:
        utils.log_warn("Exit No Inject")
        exit()
    data = {
        "get": {
            "fields": {
                "code_serial": project_id
            }
        }
    }
    token_data = inject_token(data)
    if not token_data:
        return False
    return token_data