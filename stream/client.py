import socket, time

"""
1) Ref
https://clay-atlas.com/blog/2019/10/15/python-chinese-tutorial-socket-tcp-ip/


2) Commands
"""

class Client:

    def __init__(self):

        self.host = '127.0.0.1'
        self.port = 9999

    def send_endpoint(self):

        client_msg = 'hello from client! '

        counter = 0
        
        while True:
            _client_msg = client_msg + str(counter)
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ### NOTE : here we use client.connect, rather than client.bind()
            client.connect((self.host, self.port))
            client.sendall(_client_msg.encode())
            time.sleep(3)
            counter += 1

if __name__ == '__main__':
    c = Client()
    c.send_endpoint()


