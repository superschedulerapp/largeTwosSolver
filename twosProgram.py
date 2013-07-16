import math

def reducit(Num,K):
    return int(Num/(10**(int(math.log(Num)/math.log(10))-K+1)))

def lastDigs(Num,k):
    return int(Num%(10**k))

def myFront(x,k=9):
    return reducit(data[modulo*(x/modulo)][0]*data[10000*((x%modulo)/10000)][0]*data[(x%modulo)%10000][0],k)


def myEnd(x,k=9):    
   return lastDigs(data[modulo*(x/modulo)][1]*data[10000*((x%modulo)/10000)][1]*data[(x%modulo)%10000][1],k)

if __name__ == '__main__':
    T = input()
    cons = {}
    maxi = 0
    for x in range(T):
        cons[x] = map(int,raw_input().split(' '))
        if cons[x][0] > maxi: maxi = cons[x][0]
    modulo = int(2*math.sqrt(maxi))
    base = (reducit(2**modulo,25),lastDigs(2**modulo,25))
    data = {0:(1,1)}    
    for x in range(1,min(modulo,10000)):
        data[x] = reducit(2*data[x-1][0],25),lastDigs(2*data[x-1][1],25)
#    b2 = (reducit(2**10000,25),lastDigs(2**10000,25))
    for x in range(10000,modulo,10000):
        data[x] = reducit(b2[0]*data[x-10000][0],25),lastDigs(b2[1]*data[x-10000][1],25)
    for x in range(modulo,maxi+1,modulo):
        data[x] = reducit(base[0]*data[x-modulo][0],25),lastDigs(base[1]*data[x-modulo][1],25)
    for i in range(T):
        n,k = cons[i]
       print myFront(n-1,k),myEnd(n-1,k)
        print myFront(n-1,k)+ myEnd(n-1,k)
