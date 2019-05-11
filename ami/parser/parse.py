from ami.libs import utils


def get_repo():
    return  utils.nvc_repo()

def initial_parse(ami_json):
    repo = get_repo()
    github_url = None
    initial_data = dict()
    for i in ami_json:
        data = dict()
        for a in repo:
            github_url = repo[a][i]['url']
            parameter = repo[a][i]['parameters']
            for params in parameter:
                params_value = None
                try:
                    params_value = ami_json[i][params]
                except Exception:
                    params_value = None
                if params_value is None:
                    params_value = parameter[params]['default']
                data[params] = params_value
        initial_data={
            "github": github_url,
            "playbook": data
        }
    return initial_data
