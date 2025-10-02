import time
from datetime import datetime

sec = 5
for i in range(sec):
    current_time = datetime.now()
    print("Текущее время:", current_time)
    time.sleep(1)