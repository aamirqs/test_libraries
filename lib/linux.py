from lib.test_support import *
import pexpect


class Linux(TestSupport):
    def __init__(self, host_ip, ssh_username, ssh_password, ssh_port=22):
        self.host_ip = host_ip,
        self.ssh_username = ssh_username,
        self.ssh_password = ssh_password
        self.ssh_port = ssh_port

    def connect(self):
        pass

    def command(self):
        pass
