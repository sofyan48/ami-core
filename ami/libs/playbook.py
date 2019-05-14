from ami.libs import utils

app_dir = utils.app_cwd()
ami_file = app_dir+"/ami.yml"

def playbook_create(json):
    try:
        utils.yaml_writeln(json, ami_file)
    except Exception as e:
        utils.log_err(e)
    else:
        return True

