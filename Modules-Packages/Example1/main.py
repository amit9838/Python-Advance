import sys

print("===========================")
print("Running main.py  -  module name {0}".format(__name__))

import module1


module1.pprint_dict("main.globals",globals())


print("importing module1 again...")
import module1

print("\n\n")
# print(module1.)
print(sys.path)
print(sys.prefix)
print("===========================")