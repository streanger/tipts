import time
import hashlib
from statistics import mean

"""
execution times (regular Python):
    1) elasped: 1.9150[s]
    2) elasped: 2.1024[s]
    3) elasped: 2.0985[s]
    4) elasped: 2.0984[s]
    5) elasped: 2.0940[s]
    6) elasped: 2.1006[s]
    7) elasped: 2.0769[s]
    8) elasped: 2.0542[s]
    9) elasped: 2.0151[s]
    10) elasped: 2.0133[s]
    mean_time: 2.0568[s]

execution times (mypyc):
    1) elasped: 1.8819[s]
    2) elasped: 2.0633[s]
    3) elasped: 2.0370[s]
    4) elasped: 2.0426[s]
    5) elasped: 2.0512[s]
    6) elasped: 2.0555[s]
    7) elasped: 2.0345[s]
    8) elasped: 2.0228[s]
    9) elasped: 1.9793[s]
    10) elasped: 1.9798[s]
    mean_time: 2.0148[s]

execution times (nuitka):
    1) elasped: 1.8237[s]
    2) elasped: 2.0070[s]
    3) elasped: 1.9987[s]
    4) elasped: 2.0082[s]
    5) elasped: 2.0388[s]
    6) elasped: 2.0188[s]
    7) elasped: 2.0055[s]
    8) elasped: 1.9827[s]
    9) elasped: 1.9543[s]
    10) elasped: 1.9342[s]
    mean_time: 1.9772[s]

info:
    -it may be the case that type annotations are not ok for mypyc

"""

def sha256_sum(content: bytes) -> str:
    """calc sha256 sum of content
    
    content is type of bytes
    keywords: sha256, hash
    """
    sha256_hash: str = hashlib.sha256(content).hexdigest()
    return sha256_hash
    
    
def create_data() -> bytes:
    data: bytes = b'A' * (1*1024*1024*1024)
    return data
    

all_executions = []
for x in range(10):
    start = time.time()
    data = create_data()
    chunks = [data[n:n+1024] for n in range(0, len(data), 1024)]
    for chunk in chunks:
        sha256_sum(chunk)
        
    stop = time.time()
    elapsed = stop-start
    all_executions.append(elapsed)
    print(f'{x+1}) elasped: {elapsed:.4f}[s]')

mean_time = mean(all_executions)
print(f'mean_time: {mean_time:.4f}[s]')
