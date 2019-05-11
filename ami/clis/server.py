from ami.clis.base import Base
from signal import signal, SIGINT
from agent import create_app
from ami.libs import utils
import os


class Server(Base):
    """
        usage:
            server start [-e | --deployment]
            server stop

        Run ami server

        Options:
        -h --help                                   Print usage
        -e --deployment                             Environment
    """
    def execute(self):
        if self.args['start']:
            app = create_app()
            env = False
            if self.args['--deployment']:
                env = True
            utils.log_rep("ctrl+c to exit")
            app.run(
                host="0.0.0.0" ,
                port=34000,
                debug= env,
            )
            exit()
