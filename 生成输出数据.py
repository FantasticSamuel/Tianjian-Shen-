import sys
import os

for i in range(2,4):
    os.system("python samplecode.py < %d.in > %d.out" % (i, i))
