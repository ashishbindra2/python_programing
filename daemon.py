from threading import *
import time

def job():
    for i in range(10):
        print('Lazy Thread')
        time.sleep(2)

t = Thread(target=job)
t.daemon = True
t.start()

time.sleep(10)
print(t.daemon)
print("End of main thread")