from ami.clis.base import Base
from signal import signal, SIGINT
from ami.libs import utils
from ami.parser import parse
from ami.libs import ansible_lib, playbook
import yaml, os

class Playbook(Base):
    """
        usage:
        playbook configure [-f FILE]
        playbook start [-f FILE]
        playbook create

        Run ami playbook [command] [option]

        Options:
        -f file --file=FILE                                        File
        -i inventory --inventory=INVENTORY                         Inventory
        -h --help                                                  Print usage
    """
    def execute(self):
        app_dir = utils.app_cwd
        playbook_dir = parse.playbook_dir
        if self.args['create']:
            utils.log_rep("Nothing To Future")
            exit()
        if self.args['configure']:
            path = None
            if self.args['--file']:
                path = utils.yaml_read(self.args['--file'])
            else:
                path = utils.yaml_read("ami.yml")
            initial_data = parse.initial_parsed(path)
            try:
                parse.initial_tree(initial_data)
            except Exception as e:
                utils.log_err(e)
            else:
                utils.log_rep("Playbook Configured")
            exit()
        if self.args['start']:
            path = None
            if self.args['--file']:
                ami_file = self.args['--file']
            else:
                ami_file = playbook_dir+"/ami.yml"
            # # ami_file = utils.yaml_read("ami.yml")
            # # ansible_lib.play_book(playbook=ami_file, inventory=app_dir+"/inventory")
            ansible_lib.playbook_file(playbook=ami_file, inventory=playbook_dir+"/inventory")
            exit()
