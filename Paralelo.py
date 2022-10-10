import http.client
import time
from threading import Thread

def doTask(id):

  conn = http.client.HTTPSConnection("dice-roll.p.rapidapi.com")
  
  headers = {
      'X-RapidAPI-Key': "c1a0017ccdmsh8ae8becfa8712f6p1baee6jsna7a4290906f6",
 'X-RapidAPI-Host': "dice-roll.p.rapidapi.com"
      }

  conn.request("GET", "/roll/4/d/20", headers=headers)
  
  res = conn.getresponse()
  data = res.read()

  print(data.decode("utf-8"))



start = time.time()

threads = []
for i in range(10):
  t = Thread(target=doTask, args=(i, ))
  threads.append(t)
  t.start()
  
for t in threads:
  t.join()

end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
