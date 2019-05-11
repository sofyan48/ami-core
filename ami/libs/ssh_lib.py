from os import chmod, system, remove
from Crypto.PublicKey import RSA
from ami.libs import utils


def create_openssh_keygen():
    key = RSA.generate(2048)
    privatekey = key.exportKey('PEM')
    pubkey = key.publickey()
    publickey = pubkey.exportKey('OpenSSH')
    return privatekey, publickey

def import_ssh_key(users):
    privkey, pubkey = create_openssh_keygen()
    path_home = "/home/"+users+"/.ssh/ami"
    with open(path_home, 'wb') as content_file:
        chmod(path_home, 0o600)
        content_file.write(privkey)
    utils.create_file("authorized_keys", "/root/.ssh", pubkey)

def create_ssh_key_command(users):
    command= 'ssh-keygen -b 2048 -t rsa -f /home/'+users+'/.ssh/ami_key -q -N ""'
    system(command)

def ssh_key_to_root(users):
    command= 'sudo cp /home/'+users+'/.ssh/ami_key.pub /root/.ssh/authorized_keys'
    system(command)

def remove_ssh_key(users):
    path_file_private = '/home/'+users+'/.ssh/ami_key'
    path_file_public = '/home/'+users+'/.ssh/ami_key.pub'
    remove(path_file_private)
    remove(path_file_public)
