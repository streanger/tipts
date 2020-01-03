import time

def time_temp():
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    return now
    
now = time_temp()
print(now)
