import pandas as pd
from rich import print

data = [
    {'some':1, 'thing':2},
    {'some':2, 'thing':3},
    {'some':3.5, 'thing':4.2},
    {'some':3.6, 'thing':4.7},
]
df = pd.DataFrame(data)
df.index += 1

md = df.to_markdown()
print(md)
print()

dict_map = {1.0: 'now', 2.0: 'later', 3.5: 'never', 4.0: 'end'}
df['last'] = df['some'].map(dict_map)
md = df.to_markdown()
print(md)
