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


multi threading
https://github.com/yennanliu/utility_Python/blob/master/multi_treading/multi_thread2.py
https://blog.louie.lu/2017/08/01/%e4%bd%a0%e6%89%80%e4%b8%8d%e7%9f%a5%e9%81%93%e7%9a%84-python-%e6%a8%99%e6%ba%96%e5%87%bd%e5%bc%8f%e5%ba%ab%e7%94%a8%e6%b3%95-06-concurrent-futures/

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

class MyThread(threading.Thread):

   def __init__(self, threadID, name):

      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

      self.host = '127.0.0.1'
      self.port = 9999

      # define recv_bufsize, so we can really receive and cut off on each incoming event
      self.recv_bufsize = 1024

      # define a lock instance, for release, acquire
      self.lock = threading.Lock()

   def run(self):

      print ("Starting " + self.name)

      self.lock.acquire()

      self.collect_event(self.name)

      self.lock.release()

      print ("Exiting " + self.name)

   def collect_event(self, threadName):

      server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      server.bind((self.host, self.port))

      server.listen(5)

      while True:

        conn, addr = server.accept()

        print ("%s: %s" % (threadName, time.ctime(time.time())))

        clientMessage = str(conn.recv(self.recv_bufsize), encoding='utf-8')

        time.sleep(1)

        print (clientMessage)


class Server:

    def __init__(self):

        pass

    def run(self):

        threads = []

        # Create new threads
        thread1 = MyThread(1, "Thread-1")
        thread2 = MyThread(2, "Thread-2")

        # Start new Threads
        thread1.start()
        #thread2.start()

        threads.append(thread1)
        #threads.append(thread2)

        for t in threads:
            t.join()

        print ("Exiting Main Thread")

if __name__ == '__main__':
    s = Server()
    s.run()