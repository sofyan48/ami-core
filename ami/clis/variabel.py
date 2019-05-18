from ami.clis.base import Base
from signal import signal, SIGINT
from ami.libs import utils, vars_lib
import yaml
import os


class Variabel(Base):
    """
        usage:
        variabel show [-o OS]
        variabel show  [-o OS] [-p PACKAGE]

        Run ami variable [command] [option]

        Options:
        -p package --package=PACKAGE                              Show Variabel Package
        -o os --os=OS                                             Set Distro Based | yum or apt
        -h --help                                                 Print usage
    """
    def execute(self):
        if self.args['show']:
            os_name = self.args['--os']
            if self.args['--package']:
                package = self.args['--package']
                vars_lib.show_variabels(os_name, package)
                exit()
            vars_lib.show_variabels_all(os_name)
            exit()
