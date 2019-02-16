# translate elements of numpy array with dict
# https://stackoverflow.com/questions/16992713/translate-every-element-in-numpy-array-according-to-key
import numpy as np

some = np.array([1, 2, 3])
print(repr(some))
dictio = {1:10, 2:20, 3:30}

out = np.vectorize(dictio.get)(some)
print(repr(out))