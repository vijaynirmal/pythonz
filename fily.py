import fileinput

for line in fileinput.input():
    line = line.strip()
    num = fileinput.lineno()
    print ('# %2i %-40s' % (num,line))
        
