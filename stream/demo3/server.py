# python 3

import socket, threading, time

"""
CLIENT V3 : consider scalability (multi thread)
- threading

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

exitFlag = 0

class MyThread(threading.Thread):

   def __init__(self, threadID, name, counter):

      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

      self.host = '127.0.0.1'
      self.port = 9999

      # define recv_bufsize, so we can really receive and cut off on each incoming event
      self.recv_bufsize = 1024

      # define a lock instance, for release, acquire
      self.lock = threading.Lock()

   def run(self):

      print ("Starting " + self.name)

      self.collect_event(self.name)

      print ("Exiting " + self.name)

   def collect_event(self, threadName):

      server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      server.bind((self.host, self.port))
      server.listen(5)

      while True:

        conn, addr = server.accept()
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        clientMessage = str(conn.recv(self.recv_bufsize), encoding='utf-8')
        time.sleep(3)
        print (clientMessage)


class Server:

    def __init__(self):

        pass

    def run(self):

        # Create new threads
        thread1 = MyThread(1, "Thread-1", 1)
        #thread2 = MyThread(2, "Thread-2", 2)

        # Start new Threads
        thread1.start()
        #thread2.start()
        thread1.join()
        #thread2.join()

        print ("Exiting Main Thread")

if __name__ == '__main__':
    s = Server()
    s.run()