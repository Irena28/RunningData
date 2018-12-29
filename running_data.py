site_name = "coolrunning.com"

import urllib3

link = 'http://www.coolrunning.com/results/17/ct/Dec9_2017Ya_set1.shtml'       
http = urllib3.PoolManager()
r = http.request('GET', link)
RunningFile = open("RunningData","wb")
RunningFile.write(r.data)
