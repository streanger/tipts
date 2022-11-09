import struct

"""
useful:
    https://www.cprogramming.com/tutorial/floating_point/understanding_floating_point_representation.html
    https://www.geeksforgeeks.org/how-to-convert-int-to-bytes-in-python/
    https://docs.python.org/3/library/struct.html#format-characters
"""

double_number = 0x4045400000000000
# double_number = 0x403ECCCCCCCCCCCD
# double_number = 0x4033333333333333

# we know that double is 64-bits -> 8bytes
bytes_value = double_number.to_bytes(8, 'little')

# with use 'd' to unpack bytes as double
value = struct.unpack('d', bytes_value)
print(value)
