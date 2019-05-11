from ami.clis.base import Base
from signal import signal, SIGINT
from ami.libs import utils, ssh_lib
import yaml
import os


class Configure(Base):
    """
        usage:
        configure ssh [-u USER]

        Run ami configure [command] [option]

        Options:
        -u user --user=USER                                       Users
        -h --help                                                 Print usage
    """
    def execute(self):
        if self.args['ssh']:
            users = self.args['--user']
            ssh_lib.create_ssh_key_command(users)
            ssh_lib.ssh_key_to_root(users)
            exit()
