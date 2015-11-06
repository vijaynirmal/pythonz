x = input("Hey! Whats your name? ")
print ("It doesnt matter what your name is Mr." + x)
x = list("Hello")
print (x)
y = [1,2,3,4,5]
m = [6,7,8,9]
y = y + m
print (y)
y.pop()
print (y)
y.pop(0)
print (y)
y.append(10)
print (y)
z = [11,11,12]
y.extend(z)
print (y)
y.remove(11)
print (y)
m = "deerc sni-<33"
n = list(m)
print (n)
n = list(reversed(m))
print (n)
a = [5,7,4,9,100,123,1,4]
b = sorted(a)
c =  list(reversed(b))
print (a)
print (b)
print (c)
from math import pi
sentenceone = "yo how %s you man?. Do you know the value of Pi? It is %.10f"
value = ('are',pi)
newval = sentenceone % value
print (newval)




