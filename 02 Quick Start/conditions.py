'''
Created on Sep 24, 2014

@author: bsavani
'''
#!usr/bin/python3
import sys;
a = 5;
b = 10;
print(sys.version_info)
if a < b :
    print("a ({}) is less than b({})".format(a, b));
else:
    print("a ({}) is greater than b({})".format(a, b));

print("a<b" if(a<b) else "a>b");
