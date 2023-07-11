*there typically tends to be in Python, some correspondence between some top level syntax or function and some underscore method that implements that syntax or function*

~James Powell

[James Powell: So you want to be a Python expert? | PyData Seattle 2017](https://youtu.be/cKPlPJyQrt4?t=2124)

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


---

[Creating a singleton in Python](https://stackoverflow.com/a/6760726)

*Modules are imported only once, everything else is overthinking. Don't use singletons and try not to use globals.*

---

[Why are Python's 'private' methods not actually private?](https://stackoverflow.com/a/1949874)

*When I first came from Java to Python I hated this. It scared me to death.*

*Today it might just be the one thing I love most about Python.*

*Remember, encapsulation is not even weakly related to "security", or keeping the kids off the lawn. It is just another pattern that should be used to make a code base easier to understand.*

---

[What's the pythonic way to use getters and setters?](https://stackoverflow.com/a/36943813)

*The "Pythonic" way is not to use "getters" and "setters", but to use plain attributes(...)*

*If later, you want to modify the setting and getting, you can do so without having to alter user code, by using the property decorator*

---

[Why is __init__() always called after __new__()?](https://stackoverflow.com/a/674369)


*Use `__new__` when you need to control the creation of a new instance.*

*Use `__init__` when you need to control initialization of a new instance.*

*`__new__` is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.*

*In contrast, `__init__` doesn't return anything; it's only responsible for initializing the instance after it's been created.*

*In general, you shouldn't need to override `__new__` unless you're subclassing an immutable type like str, int, unicode or tuple.*

~From April 2008 post: [When to use __new__ vs. __init__?](http://mail.python.org/pipermail/tutor/2008-April/061426.html) on mail.python.org.

---

[Al Sweigart: The Amazing Mutable, Immutable Tuple](https://www.youtube.com/watch?v=argy7dRB_LI)

*Everyone knows Python tuples are immutable, but an immutable tuple that contains mutable objects is itself mutable. Or is it?*
