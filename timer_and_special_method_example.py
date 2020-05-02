import time
from threading import Thread


class Timer():
    def __init__(self, value):
        pass
        self.COUNTER_VALUE = value
        self.MINUTES_LEFT, self.SECONDS_LEFT = divmod(self.COUNTER_VALUE-1, 60)
        t = Thread(target=self.count_down)
        t.start()
        
        
    def count_down(self):
        now = time.time()
        val = self.COUNTER_VALUE        # another variable, to not depend on self.COUNTER_VALUE
        n = 1
        
        while True:
            if time.time() - now > n:
                n += 1
                val -= 1
                
            self.MINUTES_LEFT, self.SECONDS_LEFT = divmod(val-1, 60)
            if val <= 0:
                # auto reset for now
                now = time.time()
                val = self.COUNTER_VALUE
                n = 1
                
    def __str__(self):
        return '{:02}:{:02}'.format(min(self.MINUTES_LEFT, 99), self.SECONDS_LEFT)
        
        
if __name__ == "__main__":
    timer = Timer(120)
    while True:
        print(timer, end='\r', flush=True)
        time.sleep(0.01)
