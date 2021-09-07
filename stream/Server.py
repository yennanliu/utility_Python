import socket

"""
1) Ref
https://docs.python.org/3/library/socket.html
https://steelkiwi.com/blog/working-tcp-sockets/
https://clay-atlas.com/blog/2019/10/15/python-chinese-tutorial-socket-tcp-ip/

2) Commands
plz open the other terminal run below as producer
nc -lk 9999
https://github.com/yennanliu/KafkaSparkPoc/blob/main/spark/src/main/scala/com/yen/streamSocketToHDFS/streamSocketEventToHDFS.scala#L13
"""
class Server:

    def __init__(self):

        self.host = '127.0.0.1'
        self.port = 7777

    def read_endpoint(self):

        HOST = '127.0.0.1'
        PORT = 9999

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #server.bind((self.host, self.self))
        server.bind((HOST, PORT))
        server.listen(1)

        while True:

            conn, addr = server.accept()
            clientMessage = str(conn.recv(1024), encoding='utf-8')
            print('Client message is:', clientMessage)


if __name__ == '__main__':
    s = Server()
    s.read_endpoint()