import pytest
from module import *


def test_add():
    assert add(1, 2) == 3
    assert add(2, -2) == 0
    
    
def test_mul():
    assert mul(1, 1) == 1
    assert mul(3, -7) == -21
    assert mul(-3, 7) == -21
    
    
if __name__ == "__main__":
    pytest.main()
    