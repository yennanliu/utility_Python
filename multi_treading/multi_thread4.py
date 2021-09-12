#!/usr/bin/python3

# https://www.1ju.org/python/python-multithreading

import threading
import time

class MyThread4 (threading.Thread):

   def __init__(self, threadID, name, counter):

      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):

      print ("Starting " + self.name)

      #--------------------------------
      # Get lock to synchronize threads
      #--------------------------------
      threadLock.acquire()

      print_time(self.name, self.counter, 3)

      #--------------------------------
      # Free lock to release next thread
      #--------------------------------
      threadLock.release()

def print_time(threadName, delay, counter):

   while counter:

      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

if __name__ == '__main__':
   threadLock = threading.Lock()
   threads = []

   # Create new threads
   thread1 = MyThread4(1, "Thread-1", 1)
   thread2 = MyThread4(2, "Thread-2", 2)

   # Start new Threads
   thread1.start()
   thread2.start()

   # Add threads to thread list
   threads.append(thread1)
   threads.append(thread2)

   # Wait for all threads to complete
   for t in threads:
      t.join()
   print ("Exiting Main Thread")