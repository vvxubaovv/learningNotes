import socket
import socketserver
from threading import Thread
import time
import sys

def connect(ip,port):
    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.connect((ip,port))
    conn.send
    return conn
    
def ask(conn,msg):
    conn.send(msg.encode('utf8'))
    data = conn.recv(1024)
    return data
    
def tell(conn,msg):
    conn.send(msg.encode('utf8'))
    
def udpClient():
    client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    return client
    
def udpTell(client,desIp,desPort,msg):
    client.sendto(msg,(desIp,desPort))
    
def udpAsk(client,desIp,desPort,msg):
    client.sendto(msg.encode('utf8'),(desIp,desPort))
    data,addr=client.recvfrom(1024)
    return data
    
def echo(ip,port,msg):
    conn = connect(ip,port)
    print("conn:"+ip+":"+str(port))
    while True:
        data=ask(conn,msg)
        msg = data.decode('utf8')
        print("ret:"+msg)
        time.sleep(10)
        
def udpEcho(ip,port,msg):
    client=udpClient()
    print("udpClient:"+ip+":"+str(port))
    while True:
        data=udpAsk(client,ip,port,msg)
        msg = data.decode('utf8')
        print("ret:"+msg)
        time.sleep(10)
    
class MyTCPServer(socketserver.TCPServer):
    def shutdown_request(self,request):
        #覆盖父类方法,阻止父类关闭链接
        print("shutdown_request")
        pass
    
def tcpServer(ip,port,handler):
    server = MyTCPServer((ip,port),handler)
    server.serve_forever()
    
def udpServer(ip,port,handler):
    server = socketserver.UDPServer((ip,port),handler)
    server.serve_forever()
    
disConn="exit"
def echoServer(conn):
    while(True):
        print("con="+str(conn._closed))
        data = conn.recv(1024)
        msg=data.decode('utf8')
        print("msg="+msg)
        if(msg==disConn):
            break
        conn.send(data)
    
def newThread(target,*args):
    newThread = Thread(target=target,args=args)
    return newThread

class SimpleHandler(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        print(str(conn))
        #echoServer(conn)
        t=newThread(echoServer,conn)
        t.start()
      
def udpEchoServer(handler):
    data=handler.rfile.read()
    msg=data.decode('utf8')
    print("msg="+msg)
    handler.wfile.write(data)
        
class UdpSimpleHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        udpEchoServer(self)
        
if __name__=="__main__":
    opt=1
    if len(sys.argv)>1:
        opt=int(sys.argv[1])
        print("opt="+str(opt))
    if opt==1:
        tcpServer('127.0.0.1',10002,SimpleHandler)
    elif opt==2:
        echo('127.0.0.1',10002,"hello")
    elif opt==3:
        udpServer('127.0.0.1',10003,UdpSimpleHandler)
    elif opt==4:
        udpEcho('127.0.0.1',10003,"udp hello")
    else:
        print("else")
            
