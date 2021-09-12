#!/usr/bin/python3

# https://www.1ju.org/python/python-multithreading

import threading
import time

exitFlag = 0

class MyThread3 (threading.Thread):

   def __init__(self, threadID, name, counter):

      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):

      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):

   while counter:

      if exitFlag:
         threadName.exit()

      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))

      counter -= 1

if __name__ == '__main__':
    # Create new threads
    thread1 = MyThread3(1, "Thread-1", 1)
    thread2 = MyThread3(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print ("Exiting Main Thread")