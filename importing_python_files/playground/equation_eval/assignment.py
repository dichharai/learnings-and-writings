import sys
sys.path.insert(1, '/Users/dicrai/Projects/medium/importing_files_python/playground/operations')

from addition import Addition
from subtraction import Subtraction

# (3+5)-(5)
add = Addition(3,5)
sub = Subtraction(add.add(), 5)


print('add: ' + str(add.add()))
print('subtract: '+ str(sub.subtract()))
