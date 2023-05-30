
*there typically tends to be in Python, some correspondence between some top level syntax or function and some underscore method that implements that syntax or function*

~James Powell

[James Powell: So you want to be a Python expert? | PyData Seattle 2017](https://youtu.be/cKPlPJyQrt4?t=2124)

---

**Example to show the above concept**

```python
class Some:
    def __init__(self):
        self.items = [1,2,3,4]
        
    def __call__(self):
        print('hello there')
        
    def __equal__(self, other):
        return self.items == other.items
        
    def __getitem__(self, index):
        return self.items[index]
        
some = Some()
```

relations between dunder (double underscore) methods and top level syntax:
- `__call__` -> `some()`
- `__equal__` -> `some == other`
- `__getitem__` -> `some[4]`, `list(some)`
- `...`
