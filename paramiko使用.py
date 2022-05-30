# -*- coding:utf-8 -*-
import paramiko
import time
l = ['10.79.233.81']
def exec_command(host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(username='gatling',password='gatling520',port=22,hostname=host,timeout=5,look_for_keys=False)
    stdin,stdout,stderr = ssh.exec_command('cd ~;source .bashrc',get_pty=True)
    res = stdout.read().decode()
    print(res)
    time.sleep(2)
    ssh.close()
if __name__ == '__main__':
    for i in l:
        print(i)
        exec_command(i)
        print('succeed')
