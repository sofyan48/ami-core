from ami.clis.base import Base
from signal import signal, SIGINT
from agent import create_app
from ami.libs import utils, ssh_lib
import yaml
import os


class Remove(Base):
    """
        usage:
        remove ssh [-u USER]

        Run ami remove [command] [option]

        Options:
        -u user --user=USER                                       Users
        -h --help                                                 Print usage
    """
    def execute(self):
        if self.args['ssh']:
            users = self.args['--user']
            ssh_lib.remove_ssh_key(users)
            exit()
