from celery import Celery
from tasks import add
import time
result = add.delay(4,4)

print("Waiting result...")
while not result.ready():
  print(time.now(),"not ready...")
  time.sleep(1)
  
print("Result:",result.get())

#from tasks import add
#add.delay(4, 6)
