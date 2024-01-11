import sys
from rich import print

# sys.flags.interactive
keys = list(sys.flags.__match_args__)
values = list(sys.flags)
flags = dict(zip(keys, values))
print(flags)
