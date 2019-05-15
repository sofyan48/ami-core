from ami.clis.base import Base
from signal import signal, SIGINT
from ami.libs import utils
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
        pass
