'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M is 3 times N .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

 Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of N and M .

Constraints
5 < N < 101
15 < M < 303

Output Format

Output the design pattern.

Sample Input

9 27

Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

'''

N, M = map(int,raw_input().split()) # for python 3 use input inplace of raw_input
for i in xrange(1,N,2): # for python 3 just use range instead of xrange
    print ((i*".|.").center(M, '-'))
print ("WELCOME".center(M, '-'))
for i in xrange(N-2,-1,-2): 
    print ((i*".|.").center(M, '-'))

# Python 3 version

N, M = map(int, input().split())
for i in range(1,N,2):
    print((i*".|.").center(M,'-'))
print ("WELCOME".center(M, '-'))
for i in range(N-2,-1,-2):
    print((i*".|.").center(M, '-'))
