#!/bin/python
import httplib2
import json
import time
import datetime
import sys
import getopt
import threading
import random

def get():
    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"
    
    try:
      opts, args = getopt.getopt(sys.argv[1:],"hu:p:")
    except getopt.GetoptError:
      print 'test.py -u url -p port -h'
      sys.exit(2)

    for o,a in opts:
     #print 'o = ' + o + 'a = ' + a
     if o == '-u':
      url = a
     if o == '-p':
      port = a

    headers = {'Content-Type': content_type_header}

    while True:
        response, content = http.request( url, 'GET', headers=headers)
        print (response)
        parsed = json.loads(content)
        print json.dumps(parsed)
        time.sleep(random.randint(0, 10))

if __name__ == '__main__':
  threads = []
  for i in range(50):
    t = threading.Thread(target=get)
    threads.append(t)
    t.start()
