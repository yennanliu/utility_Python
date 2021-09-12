# python 3

import socket, time, random

"""
CLIENT V2 : consider scalability (multi thread)

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

        self.client_msgs1 = [
                            'hello from client! ',
                            '123456 ',
                            'aaabbbccc abc abc ',
                            ' ??? ',
                            ''
                            ]

        self.client_msgs2 = [
                             {"timetamp":1629857927,"user_id":"u0001","event_type":"login","platform":"mobile","os":"ios","version":"ios-11"},
                             {"timetamp":1629857927,"user_id":"u0002","transaction_id":"t001","event_type":"payment","platform":"mobile","os":"ios","version":"ios-11"},
                             {"timetamp":1629857927,"user_id":"u0003","transaction_id":"","event_type":"register","platform":"mobile","os":"android","version":"pixel"}
                             ]

    def run(self):

        msgs = self.client_msgs2

        counter = 0
        
        while True:
            client_msg = msgs[random.randint(0, len(msgs)-1)]

            # create some randomness in data
            client_msg['user_id'] = random.randint(1, 100)
            client_msg['timetamp'] = random.randint(1629850000, 1629857927)

            _client_msg = str(client_msg) + "\n"
            print ("counter = ", str(counter), _client_msg)
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ### NOTE : here we use client.connect, rather than client.bind()
            client.connect((self.host, self.port))
            client.sendall(_client_msg.encode())
            time.sleep(1)
            counter += 1

if __name__ == '__main__':
    c = Client()
    c.run()