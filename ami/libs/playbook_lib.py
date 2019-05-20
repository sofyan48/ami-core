from ami.libs import utils

app_dir = utils.app_cwd


def playbook_create(json, app_name):
    ami_file = app_dir+"/"+app_name+"/ami.yml"
    try:
        utils.yaml_writeln(json, ami_file)
    except Exception as e:
        utils.log_err(e)
    else:
        return True


def playbook_remove(path):
    try:
        utils.rm_dir(path)
    except Exception as e:
        utils.log_err(e)
    else:
        return True


