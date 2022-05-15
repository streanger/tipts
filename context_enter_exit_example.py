
class Some():
    def __enter__(self):
            print('hello')
            
    def __exit__(self, *exc):
            print('bye')
            
some = Some()
with some as s:
    print(42)
    
"""
https://docs.python.org/3/library/contextlib.html
"""
