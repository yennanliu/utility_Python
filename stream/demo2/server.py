# python 3

import socket
from _thread import start_new_thread
import threading

"""
SERVER V2 : consider scalability (multi thread)
    - via _thread

- Ideas
    - multi thread
        - https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
    - async
    - file IO enhancement

1) Ref

Sockets are byte streams, not message streams
http://stupidpythonideas.blogspot.com/2013/05/sockets-are-byte-streams-not-message.html
https://www.1ju.org/python/python-multithreading

https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data

socket
https://www.1ju.org/python/python-networking

2) Commands
python server.py

3) client.py
https://github.com/yennanliu/utility_Python/blob/master/stream/client.py

4) QA 
plz use below curl commands send data via CLI
curl -d "param1=value1&param2=value2" -X POST http://localhost:9999
curl -d "123123" -X POST http://localhost:9999
curl -d "HELLO WORLD" -X POST http://localhost:9999

5) clear app using port
lsof -i tcp:<port> 
"""

class Server:

    def __init__(self):

        self.host = '127.0.0.1'
        self.port = 9999

        # define recv_bufsize, so we can really receive and cut off on each incoming event
        self.recv_bufsize = 1024

        # define a lock instance, for release, acquire
        self.lock = threading.Lock()

    def threaded(self, conn, threadName):
        

        # acquire lock
        self.lock.acquire()

        clientMessage = str(conn.recv(self.recv_bufsize), encoding='utf-8')
        #print ("thread id :", threading.current_thread().name)
        print ("thread name :", threadName)

        # release lock
        self.lock.release()
        
        #conn.close()

    def run(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)

        while True:
            conn, addr = server.accept()
            """
            https://docs.python.org/3/library/socket.html

            socket.recv(bufsize[, flags])
            Receive data from the socket. 
            The return value is a bytes object representing the data received. 
            The maximum amount of data to be received at once is specified by bufsize. 
            """

            # get lock
            start_new_thread(self.threaded, (conn, "thread-1"))
            start_new_thread(self.threaded, (conn, "thread-2"))
            start_new_thread(self.threaded, (conn, "thread-3"))
            #start_new_thread(self.threaded, (conn,))

            clientMessage = str(conn.recv(self.recv_bufsize), encoding='utf-8')
            print("thread name : " + threading.current_thread().name + " , clientMessage : "  + clientMessage)

            # save to file
            """
            https://www.w3schools.com/python/python_file_write.asp

            "a" - Append - will append to the end of the file
            "w" - Write - will overwrite any existing content
            """
            with open('output.txt', 'a') as f:
                f.write(clientMessage)

        server.close()

if __name__ == '__main__':
    s = Server()
    s.run()