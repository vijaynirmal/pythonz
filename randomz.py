'''#electronic throwing die

import random,sys
sys.path.append('C:\\Python34\\Practice')
class randy:
    def toss(self,sides,throwz):
        sum = 0
        for x in range(throwz):
            sum += random.randrange(sides) + 1
        return sum
    

sides = int(input('Enter the number of sides of the die '))
throwz = int(input('Enter the number of throws/range '))
d = randy()
print(d.toss(sides,throwz))

# Forthune cookie program

import random,sys,fileinput
sys.path.append('C:\\Python34\\Practice')

x = list(fileinput.input())
y = random.choice(x)
print(y)'''

'''import sys
sys.path.append('C:\\Python34\\Practice')
f = open ('C:\\Python34\\Practice\\texty.txt','r+')
f.append('have some fresh air')
print (f.read())'''

'''import sys
sys.path.append('C:\\Python34\\Practice')
line_number = 0
with open('C:\\Python34\\Practice\\texty.txt') as a_file:
    for a_line in a_file:                                               
        line_number += 1
        print('%s ' ' %s' %(line_number,a_line.rstrip())) '''

import os,sys
sys.path.append('C:\\Users\\jeni\\Desktop\\Music\\Aug')
os.startfile('C:\\Users\\jeni\\Desktop\\Music\\Aug\\Oboma Bilgates.mp3')





