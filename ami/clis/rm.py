from ami.clis.base import Base
from signal import signal, SIGINT
from ami.libs import utils
import yaml
import os


class Rm(Base):
    """
        usage:
        rm

        Run ami rm [command] [option]

        Options:
        -h --help                                                 Print usage
    """
    def execute(self):
        utils.log_warn("Under Construction")
