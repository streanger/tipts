'''
version: 1.1
21.05.2020, 01:11
'''

import time
from threading import Thread


class TimerClass():
    '''timer class with functions such as:
        -start
        -stop
        -cancel
        -reset
        
    '''
    
    def __init__(self, value):
        # ******** define attributes ********
        self.n_minus_one_mode = False
        self.start_flag = False
        self.stop_flag = False
        self.continue_flag = False
        self.auto_trigger = False
        self.interval = value
        self.minutes_left, self.seconds_left = divmod(self.interval-1, 60)
        self.init = 0
        self.elapsed = 0
        
        
        # ******** start timer thread ********
        self.count_thread = Thread(target=self.count_down_loop)
        self.count_thread.start()
        
        
    def count_down_loop(self):
        '''count down in inifinite loop'''
        while True:
            self.init = time.time()
            begin = time.time()
            interval = self.interval        # another variable, to not depend on self.interval
            # n = 1
            
            if not self.start_flag:
                time.sleep(0.001)
                # print('wait for start')
                continue
                
            while True:
                # if auto reset, rotate in this loop and refer to the upper value
                # in other case (manual reset), break this loop, and set begin time again
                
                if self.continue_flag:
                    # setup for begin time
                    pass
                    self.stop_flag = False
                    self.continue_flag = False
                    interval = elapsed
                    begin = time.time()
                    
                if self.stop_flag:
                    # print('stop')
                    continue
                    
                    
                time.sleep(0.001)
                elapsed = interval - (time.time() - begin)
                self.elapsed = elapsed
                rounded = round(elapsed)
                self.minutes_left, self.seconds_left = divmod(rounded, 60)
                
                # print('elapsed: {}'.format(elapsed))
                if elapsed <= 0:
                    # auto reset for now
                    begin = time.time()
                    interval = self.interval
                    
                    print('diff (now - init): {}'.format(time.time() - self.init))
                    
                '''
                if time.time() - now > n:
                    n += 1
                    val -= 1
                    
                self.minutes_left, self.seconds_left = divmod(val-1, 60)
                if val <= 0:
                    # auto reset for now
                    now = time.time()
                    val = self.interval
                    n = 1
                    print('diff (now - init): {}'.format(time.time() - self.init))
                '''
                
        return None
        
        
    def timer_reset(self):
        '''reset timer to interval value and start to count again'''
        pass
        print('timer reset')
        
        
    def timer_start(self):
        '''if waits for start, it starts; in other case, do nothing'''
        pass
        self.start_flag = True
        print('timer start')        
        
        
    def timer_stop(self):
        '''stop timer if it works for now'''
        pass
        self.stop_flag = True
        print('timer stop')
        
        
    def timer_continue(self):
        '''continue with counting after previous stop; in other case do nothing'''
        pass
        self.continue_flag = True
        print('timer continue')
        
        
    def timer_cancel(self):
        '''go to the last value and wait for start, to run'''
        pass
        print('timer cancel')
        
        
    def __str__(self):
        return '{:02}:{:02}'.format(min(self.minutes_left, 99), self.seconds_left)
        
        
if __name__ == "__main__":
    timer = TimerClass(30)
    timer.timer_start()
    
    print(timer.elapsed)
    time.sleep(1)
    print(timer.elapsed)
    timer.timer_stop()
    time.sleep(2)
    print(timer.elapsed)
    time.sleep(1)
    
    timer.timer_continue()
    print('after continue: {}'.format(timer.elapsed))
    
    
    # while True:
        # print(timer, end='\r', flush=True)
        # time.sleep(0.001)
        
        