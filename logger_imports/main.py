from logger import log
from a import a_verbose
from b import b_verbose
from c import c_verbose

print(log.verbose)
a_verbose()
b_verbose()
c_verbose()

log.verbose = False

print(log.verbose)
a_verbose()
b_verbose()
c_verbose()
