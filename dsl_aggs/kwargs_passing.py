

class Some():
    def bucket(self, pos1, pos2, kw1=0, kw2=1, kw3=2):
        print('FROM BUCKET')
        print(f'    {pos1=}')
        print(f'    {pos2=}')
        print(f'    {kw1=}')
        print(f'    {kw2=}')
        print(f'    {kw3=}')
        print()
        
    def metric(self, pos1, pos2, kw1=3, kw2=4, kw3=5):
        print('FROM METRIC')
        print(f'    {pos1=}')
        print(f'    {pos2=}')
        print(f'    {kw1=}')
        print(f'    {kw2=}')
        print(f'    {kw3=}')
        print()

items = [
    ('bucket', 'pos1-a', 'pos2', {'kw1': 43}),
    ('bucket', 'pos1-b', 'pos2', {'kw1': 44, 'kw2': 45}),
    ('metric', 'pos1-c', 'pos2', {'kw1': 46, 'kw2': 47, 'kw3': 48}),
    ('metric', 'pos1-d', 'pos2', {'kw1': 49}),
]

some = Some()
for method, *args, kwargs in items:
    print(f'{method=}')
    print(f'{args=}')
    print(f'{kwargs=}')
    print()
    getattr(some, method)(*args, **kwargs)
    input('go next ')
