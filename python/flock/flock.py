
import os
import sys
import fcntl

file = sys.argv[1]

fd = open(file, "r+")
print 'locking {}...'.format(file),
sys.stdout.flush()

fcntl.flock(fd.fileno(), fcntl.LOCK_EX)

print 'ok'


while(True):
    pass


fd.close()



