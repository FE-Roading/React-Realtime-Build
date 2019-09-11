#!/usr/bin/python3

from fabric import Connection
import os

def getEnvValue(key):
    return os.environ[key]

config = {
    "host": "127.0.1.1",
    "port": 22,
    "user": getEnvValue("TEST_USER"),
    "password": getEnvValue("TEST_PASSWD"),
    "git": "https://github.com/FE-Roading/React-Realtime-Build.git",
    "projectName": "React-Realtime-Build",
    "dist": "/home/www/"
}

def main():
    # �����ĵ�������ssh�������¼���Ͳ���Ҫ connect_kwargs ��ָ�������ˡ�
    c = Connection("{}@{}:{}".format(config["user"], config["host"], config["port"]), connect_kwargs={"password": config["password"]})

    with c.cd(config["dist"]):        
        c.run("rm -rf test")
        c.run("rm -rf {}".format(config["projectName"]))        
        c.run("git clone {}".format(config["git"]), pty= True) 
        c.run("mv {} test".format(config["projectName"]))

    with c.cd("/home/www/test"):
        print("������ȥ��ɣ����ڰ�װ����")
        c.run("npm install")
        print("������װ��ɣ����ڹ�����Ŀ")
        c.run("npm run build")
        print("��Ŀ�ѹ�����ɣ�")

if __name__ == '__main__':
    main()
