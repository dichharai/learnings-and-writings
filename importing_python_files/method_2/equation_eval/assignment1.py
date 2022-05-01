#!/usr/bin/python3

#import sys
#sys.path.insert(1,'/Users/dicrai/Projects/medium/importing_files_python/method-1/operations')
from addition import add
from subtraction import subtract

# (3+5)-(5)
def eval_1():
    res = subtract(add(3,5), 5)
    print(res)

eval_1()
