import Utils
import threading
import Companies
import time

time_delta = 10

class UpdaterThread(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
      print ("Starting " + self.name)
      update(self)
      print ("Exiting " + self.name)

def update(updater_thread):
   while 1:
      time.sleep(time_delta)
      Companies.update_company_information()
      
