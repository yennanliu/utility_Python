import socket

"""
1) Ref
https://clay-atlas.com/blog/2019/10/15/python-chinese-tutorial-socket-tcp-ip/

https://docs.python.org/3/library/socket.html
https://steelkiwi.com/blog/working-tcp-sockets/

2) Commands
python server.py

3) client.py
https://github.com/yennanliu/utility_Python/blob/master/stream/client.py

4) QA 
plz use below curl commands send data via CLI
curl -d "param1=value1&param2=value2" -X POST http://localhost:9999
curl -d "123123" -X POST http://localhost:9999
curl -d "HELLO WORLD" -X POST http://localhost:9999
"""
class Server:

    def __init__(self):

        self.host = '127.0.0.1'
        self.port = 9999

    def read_endpoint(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(1)

        while True:
            conn, addr = server.accept()
            clientMessage = str(conn.recv(1024), encoding='utf-8')
            print('Client message is:', clientMessage)

            # save to file
            with open('output.txt', 'a') as f:
                f.write(clientMessage)
        f.close()

if __name__ == '__main__':
    s = Server()
    s.read_endpoint()