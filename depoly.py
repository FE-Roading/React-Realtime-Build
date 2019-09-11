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
    # 如果你的电脑配了ssh免密码登录，就不需要 connect_kwargs 来指定密码了。
    c = Connection("{}@{}:{}".format(config["user"], config["host"], config["port"]), connect_kwargs={"password": config["password"]})

    with c.cd(config["dist"]):        
        c.run("rm -rf test")
        c.run("rm -rf {}".format(config["projectName"]))        
        c.run("git clone {}".format(config["git"]), pty= True) 
        c.run("mv {} test".format(config["projectName"]))

    with c.cd("/home/www/test"):
        print("代码拉去完成，正在安装依赖")
        c.run("npm install")
        print("依赖安装完成，正在构建项目")
        c.run("npm run build")
        print("项目已构建完成！")

if __name__ == '__main__':
    main()
