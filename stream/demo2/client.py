import socket, time

"""
CLIENT V2 : consider scalability

1) Ref

https://clay-atlas.com/blog/2019/10/15/python-chinese-tutorial-socket-tcp-ip/

2) Commands
python client.py

3) server.py
https://github.com/yennanliu/utility_Python/blob/master/stream/server.py
"""

class Client:

    def __init__(self):

        self.host = '127.0.0.1'
        self.port = 9999

    def send_endpoint(self):

        client_msg = 'hello from client! '

        counter = 0
        
        while True:
            _client_msg = client_msg + str(counter) + "\n"
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ### NOTE : here we use client.connect, rather than client.bind()
            client.connect((self.host, self.port))
            client.sendall(_client_msg.encode())
            time.sleep(3)
            counter += 1

if __name__ == '__main__':
    c = Client()
    c.send_endpoint()