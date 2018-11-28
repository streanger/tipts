'''
multiple subplots
'''

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
t3 = np.arange(0.0, 5.0, 0.01)

dataSet = [(t1, f(t1), 'bo', t2, f(t2), 'k'),
           (t2, np.sin(np.pi*t2), 'g--'),
           (t3, np.cos(2*np.pi*t3), 'r--')]

plt.figure(1)
plt.subplot(411)            # 311 -> 1st digit - number of rows, 2nd - number of col, 3rd - number of element if row
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(412)
plt.plot(t2, np.sin(np.pi*t2), 'g--')

plt.subplot(413)
plt.plot(t3, np.cos(2*np.pi*t3), 'r--')

plt.subplot(414)
plt.plot(t3, np.cos(2*np.pi*t3), 'r--')
plt.show()


# for *args, **kwargs in dataSet:
    # print(*args, **kwargs)
