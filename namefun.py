


name = input ("Enter the name: ")

def build(dictionary,name) :
    labels = ['first','middle','last']
    namelist = name.split()
    if len(namelist) == 2 :
            namelist = namelist[0] + ' ' + namelist[1]
    for label,name in zip(labels,namelist) :
        new = dict(zip(namelist,name))
    newone = dict(zip(storage,new))
    return newone

print (build(name))
   
