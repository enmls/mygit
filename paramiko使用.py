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
        
        
        
 #################################################################################################################
# -*- coding:utf-8 -*-
import paramiko
import time
l = ['10.79.233.81']
def sftp_client_open(host,file_name,mode_method):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username='gatling', password='gatling520')
    ftp = ssh.open_sftp()
    file=ftp.file(file_name, mode=mode_method, bufsize=-1)
    file.write('export JAVA_HOME=/app/gatling/project/jdk1.8.0_311\nexport PATH=$JAVA_HOME/bin:$PATH\nexport CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar')
    file.flush()  #写出写缓冲区中的任何数据。如果未打开写缓冲，这可能无济于事
    time.sleep(1)
    ftp.close()
    ssh.close()
if __name__ == '__main__':
    for ip in l:
        sftp_client_open(ip,'/app/gatling/.bashrc',"a+")
        
        
#########################################################################################################################
# -*- coding:utf-8 -*-
import paramiko
import time
l = ['10.79.233.81']
def exec_command(host,command_exc):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(username='root',password='123456',port=22,hostname=host,timeout=5,look_for_keys=False)
    stdin,stdout,stderr = ssh.exec_command(command_exc,get_pty=True)
    res = stdout.read().decode()
    print(res)
    time.sleep(5)
    ssh.close()
def sftp_client_put(host,local_path,remote_path):
    # 1 创建transport通道
    tran = paramiko.Transport((host,22))
    tran.connect(username='gatling', password='gatling520')
    # 2 创建sftp实例
    sftp = paramiko.SFTPClient.from_transport(tran)
    # 3 执行上传功能
    put_info = sftp.put(local_path, remote_path, confirm=True)
    print(put_info)
    print(f"上传{host}----{local_path}完成")
    # 5 关闭通道
    tran.close()
import os,sys
path = os.getcwd()
path1 = os.listdir()
pcmpath = os.path.join(path,'jdk-8u311-linux-x64.tar.gz')
print(pcmpath)
if __name__ == '__main__':
    for ip in g520:
        sftp_client_put(ip,pcmpath,'/app/gatling/project/jdk-8u311-linux-x64.tar.gz')
        

        
        
 
###############################################################################################
