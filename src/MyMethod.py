def myabs(a):
    if(a>0):
        return a
    elif(a < 0):
        return -a

def table(n):
    for x in range (1,n+1):
        for y in range(1,x+1):
            print('%d*%d=%d\t'%(y,x,x*y),end="")
        print()