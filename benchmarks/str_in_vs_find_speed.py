# text = 'text without pattern'*1000 + 'this is spam here'
text = 'this is spam here'
pattern = 'spam'

# ***** pattern in text *****
# python -m timeit -n 10000000 -s "text = 'this is spam here'; pattern = 'spam'" "pattern in text"
# 10000000 loops, best of 5: 30.8 nsec per loop

# ***** find *****
# python -m timeit -n 10000000 -s "text = 'this is spam here'; pattern = 'spam'" "(text.find(pattern) > -1)"
# 10000000 loops, best of 5: 80.8 nsec per loop
