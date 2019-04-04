#encoding=utf8
import socket
import subprocess
import time
from threading import Thread

proxy_ip = "127.0.0.1"
proxy_port = 10086

echo_ip = "127.0.0.1"
echo_port = 10087

class SimpleServer:
    def __init__(self,ip,prot,handler):
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port
        self.handler = handler
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((ip,prot))
        self.server_socket.listen(5)
        
    def start(self):
        while True:
            conn,addr=self.server_socket.accept()
            print(str(addr)+" 连接进入:"+str(conn))
            newThread(self.handler,conn).start()

def simple_proxy_handler(conn):
    target_over=True
    target_over_word="$$over"
    while True:
        if target_over:
            data=conn.recv(1024)
            msg=data.decode('utf8')
            sp_msg=msg.split(':')
            target_ip=sp_msg[0]
            target_port=int(sp_msg[1])
            target_conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            target_conn.connect((target_ip,target_port))
            target_over=False
        while True:
            data=conn.recv(1024)
            target_conn.send(data)
            print("send:"+str(data))
            if len(data)<1024:
                break
        while True:
            data1=target_conn.recv(1024)
            conn.send(data1)
            print("recv:"+str(data1))
            if len(data1)<1024:
                break
        if data==target_over_word.encode('utf8'):
            target_conn.close()
            print("结束代理<%s:%s>..."%(target_ip,target_port))
            target_over=True
       
def simple_echo_handler(conn):
    over_word="$$over"
    while(True):
        data = conn.recv(1024)
        msg=data.decode('utf8')
        conn.send(data)
        print("echo:"+msg)
        if msg==over_word:
            conn.close()
            break
       
def newThread(target,*args):
    newThread = Thread(target=target,args=args)
    return newThread
    

def simple_client():
    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.connect((proxy_ip,proxy_port))
    exit_word="exit"
    disconn_word="disconn"
    connect = False
    while True:
        if connect:
            inp=input("input:")
        else:
            print('input ip:port to connect')
            inp=input("input:")
            if inp==exit_word:
                exit()
            conn.send(inp.encode('utf8'))
            print('connect to:'+inp)
            connect=True
        if inp==exit_word:
            exit()
        if inp==disconn_word:
            conn.send('$$over'.encode('utf8'))
            connect = False
        if connect:
            conn.send(inp.encode('utf8'))
            recv_msg=''
            while True:
                data = conn.recv(1024)
                recv_msg = recv_msg+data.decode('utf8')
                if len(data)<1024:
                    break
            print('recv:'+recv_msg)
            

if __name__=="__main__":
    proxy_server = SimpleServer(proxy_ip,proxy_port,simple_proxy_handler)
    echo_server = SimpleServer(echo_ip,echo_port,simple_echo_handler)
    newThread(proxy_server.start).start()
    newThread(echo_server.start).start()
    simple_client()
