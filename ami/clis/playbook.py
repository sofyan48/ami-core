from ami.clis.base import Base
from signal import signal, SIGINT
from agent import create_app
from ami.libs import utils
from ami.parser import parse
from ami.libs import ansible_lib
import yaml, os


class Playbook(Base):
    """
        usage:
        playbook start [-f FILE] [-i INVENTORY]

        Run ami playbook [command] [option]

        Options:
        -f file --file=FILE                                        File
        -i inventory --inventory=INVENTORY                         Inventory
        -h --help                                                  Print usage
    """
    def execute(self):
        app_dir = utils.app_cwd+"/playbook"
        if self.args['start']:
            path = None
            if self.args['--file']:
                path = utils.yaml_read(self.args['--file'])
            else:
                path = utils.yaml_read("ami.yml")
            initial_data = parse.initial_parse(path)
            github_url = initial_data['github']
            playbook = initial_data['playbook']
            checks = utils.template_git(github_url, app_dir)
            if not checks:
                utils.log_err("Repo Not Cloning")
                exit()
            checks = utils.yaml_writeln(playbook,app_dir+"/ami.yml")
            if not checks:
                utils.log_err("Playbook Not Created")
                exit()
            os.chdir(app_dir)
            ami_file = utils.yaml_read("ami.yml")
            ansible_lib.play_book(playbook=ami_file)
            exit()
