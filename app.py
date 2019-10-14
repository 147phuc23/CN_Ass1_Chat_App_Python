import socket
import threading

class Sever:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)

    def handler(self, c, a):
        while true:
            data = c.recv(1024);
            for connection in self.connection:
                connection.send(data)
            if not data:
                break
    
    def run(self):
        while true:
            c,a = self.sock.accept()
            cThread = threading.Thread(target = self.handler, args = (c, a))
            cThread.daemon = true
            self.connections.append(c)
            print(self.connections)

sever = Sever()
sever.run()


