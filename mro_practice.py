import time
from tkinter import Tk, Frame

# https://stackoverflow.com/questions/10482953/python-extending-with-using-super-python-3-vs-python-2


class A:
    def __init__(self, *args, **kwargs):
        print('A')
        super().__init__()  # comment/uncomment

class B(A):
    def __init__(self, *args, **kwargs):
        print('B')
        super().__init__()  # comment/uncomment
        # while True:
            # print('stucked in B')
            # time.sleep(2)
            
class X:
    def __init__(self, *args, **kwargs):
        print('X')
        # super().__init__()

# class Forward(list, Frame, B, X):
# class Forward(Frame, B, X):
class Forward(B, X):
    def __init__(self, master):
        print('Forward')
        # super().__init__()
        # super().__init__(master())
        B.__init__(self)
        # super().__init__(master())


class Backward(X, B):
    def __init__(self):
        print('Backward')
        super().__init__()
        
 
some = Forward(master=Tk)
# thing = Backward()
