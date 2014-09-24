'''
Created on Sep 24, 2014

@author: bsavani
'''
def isPrime(n):
    if(n == 1):
        print("1 is special case");
        return True;
    for x in range(2, n):
        if(n % x == 0):
            print("{} is not prime as it is divisible by {}".format(n, x));
            return True;
    else:
        print("{} is Prime.".format(n))
        return False;

for n in range(1, 20):
    isPrime(n)
'''
1 is special case
2 is Prime.
3 is Prime.
4 is not prime as it is divisible by 2
5 is Prime.
6 is not prime as it is divisible by 2
7 is Prime.
8 is not prime as it is divisible by 2
9 is not prime as it is divisible by 3
10 is not prime as it is divisible by 2
11 is Prime.
12 is not prime as it is divisible by 2
13 is Prime.
14 is not prime as it is divisible by 2
15 is not prime as it is divisible by 3
16 is not prime as it is divisible by 2
17 is Prime.
18 is not prime as it is divisible by 2
19 is Prime.
'''
