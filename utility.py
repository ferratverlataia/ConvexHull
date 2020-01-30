def shoelaceformulaarea(self,b):
    if type(b) != type(list()):
        return  list()
    total=0
    a1=0
    a2=0
    for i in range(0,len(n)-1):
        a1+=b[i][0]+b[i+1][1]
        a2+=b[i+1][0]+b[i][1]
    total=a1-a2
    
    return total 
