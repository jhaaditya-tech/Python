"""
In Python, we can create three ways, i.e. Collections module, Queue module and multiprocessing module

"""

#Python Collection module

"""

The collections.deque Class
Method- deque(), append(), popleft(), clear()

"""

"""

from collections import deque
customQueue=deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
#Will overwrite if appended over limit
print(customQueue)
customQueue.popleft()
print(customQueue)
customQueue.clear()

"""

#Using Queue Module

"""
FIFO queue ---- Queue(maxsize=0, making infinite quee size)
LIFO queue - Stack
Priority Queue

Method- qsize(), empty(), full, put(),get(), task_done(),join()
"""

"""
import queue as q

customQueue=q.Queue(maxsize=3)
customQueue.put(5)
customQueue.put(10)
customQueue.put(15)
print(customQueue)
"""

#Multiprocessing Model

'''
Sharing data between processors

'''
from multiprocessing import Queue
customQueue=Queue(maxsize=3)
customQueue.put(1)
customQueue.get(1)

