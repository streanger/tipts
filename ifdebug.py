import sys
import time
import ctypes

while True:
    debug_status = ctypes.windll.kernel32.IsDebuggerPresent()
    print('{} debug: {}'.format(time.strftime('%H:%M:%S'), debug_status), flush=True, end='\r')
    time.sleep(1)
    