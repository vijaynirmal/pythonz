def fibs(x) :
    fib = [0,1]
    for x in range(x - 2) :
        fib.append(fib[-2] + fib[-1])
    return fib
x = int(input ("Enter the range : "))
print (fibs(x))
        
storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

print("storage1 : ", storage)

me = 'Magnus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]

print("storage2 : ", storage)
