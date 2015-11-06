try:
    x = int(input("Enter value of x : "))
    y = int(input("Enter Value of y : "))
    z = input("Enter Value of z : ")
    print (x/z)
    print (x/y)
except ZeroDivisionError :
    print ("Second number cannot be zero ")
except ValueError :
    print("Enter a positive integer. Alpabets/words are invalid")
except TypeError :
    print("Alpabets/words are invalid")
    
import datetime
from heapq import *
x = list(range(10))
heapify(x)
print (x)
heappush(x,1)
print (x)
heappop(x)
print (x)
print (datetime.time())

'''import random
from time import *

d1 = (2005,1,1,12,12,21,0,6,256)
d2 = (2006,1,1,12,12,21,0,6,256)
t1 = mktime(d1)
t2 = mktime(d2)
z = random.uniform(d1,d2)
print (asctime(z))'''

    
