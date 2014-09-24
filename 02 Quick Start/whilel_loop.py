'''
Created on Sep 24, 2014

@author: bsavani
'''
a, b = 0, 1;
while b < 50:
    print(b);
    a, b = b, a + b;

print("DONE")


'''
1
1
2
3
5
8
13
21
34
DONE
'''