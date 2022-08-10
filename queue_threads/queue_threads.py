import sys
import time
import random
import threading
import queue
from collections import deque
from rich import print

"""
useful:
    https://stackoverflow.com/questions/35160417/threading-queue-working-example
    https://stackoverflow.com/questions/21639888/is-it-possible-to-convert-list-to-queue-in-python
    https://stackoverflow.com/questions/717148/queue-queue-vs-collections-deque
    https://stackoverflow.com/questions/52582685/using-asyncio-queue-for-producer-consumer-flow
    
think of:
    https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_pool_of_threads.htm
    
"""

class Worker(threading.Thread):
    def __init__(self, q, doing, results, *args, **kwargs):
        self.q = q
        self.doing = doing
        self.results = results
        super().__init__(*args, **kwargs)
        
    def run(self):
        while True:
            if self.q.empty():
                if not self.doing.empty():
                    # print('[cyan] wait a little bit')
                    time.sleep(0.5)
                    continue
                # print('[cyan]queue is empty')
                break
                
            # get item; try to do the job
            job = self.q.get()
            self.doing.put(job)
            time.sleep(random.randrange(20)/10)
            status = random.randint(0, 1)
            if status:
                # if works append result to results
                print('[green]job done: {}'.format(job))
                self.results.put('{} done'.format(job))
            else:
                # if won't return item to previous queue
                print('[red]job failed: {}'.format(job))
                self.q.put(job)
            self.doing.get()
            self.q.task_done()
        return None
        
        
if __name__ == "__main__":
    # ******** make queues ********
    q = queue.Queue()
    doing = queue.Queue()  # middle queue; not needed
    results = queue.Queue()
    
    # ******** make jobs ********
    jobs = ['job{}'.format(x) for x in range(1000)]
    [q.put(job) for job in jobs]  # put items into queue
    # sys.exit()

    # ******** run workers ********
    workers_number = 200
    start = time.time()
    for x in range(workers_number):
        Worker(q, doing, results).start()
        
    q.join()
    print('[gold1]well done!!!')
    print('workers_number: {}'.format(workers_number))
    print(results.qsize())
    stop = time.time()
    print('[*] elapsed: {}[s]'.format(stop-start))
    