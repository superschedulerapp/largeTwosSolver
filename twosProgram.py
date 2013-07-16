import math

def reducit(Num,K):
    '''Return only the leading K digits of a number
        by dividing the number by a sufficiently large power of 
        ten that the remaining number will be K digits after
        an integer truncation'''
    return int(Num/(10**(int(math.log(Num)/math.log(10))-K+1)))

def lastDigs(Num,k):
    '''Return only the final K digits of a number by returning the 
        modulo (remainder) of division by 10**k'''
    return int(Num%(10**k))

def myFront(x,k=9):
    '''Returns the calculation of the lead digits of a composite number, 
        where only specific values have been stored to make up any possible number'''
    return reducit(data[modulo*(x/modulo)][0]*data[10000*((x%modulo)/10000)][0]*data[(x%modulo)%10000][0],k)


def myEnd(x,k=9):    
    '''Returns the calculation of end digits of a composite number,
        where only specific values have been stored to make up any possible number'''
   return lastDigs(data[modulo*(x/modulo)][1]*data[10000*((x%modulo)/10000)][1]*data[(x%modulo)%10000][1],k)

if __name__ == '__main__':

    #Take inputs 
    T = input()
    cons = {}
    maxi = 0
    for x in range(T):
        cons[x] = map(int,raw_input().split(' '))
        if cons[x][0] > maxi: maxi = cons[x][0]

    #Initialize a few constants and the storage dictionary 
    modulo = int(2*math.sqrt(maxi))
    base = (reducit(2**modulo,25),lastDigs(2**modulo,25))
    b2 = (reducit(2**10000,25),lastDigs(2**10000,25))
    data = {0:(1,1)}    


    #Now we generate every possible power of two below the maximum. 

    #First calculate the lead and tail 25 digits for every power of two from 1-10,000.
    for x in range(1,min(modulo,10000)):
        data[x] = reducit(2*data[x-1][0],25),lastDigs(2*data[x-1][1],25)

    #Then calculate the lead and tail 25 digits for numbers starting at 10k and 
    # skipping 10,000 at a time. Because all values for 1-10000 are already stored, 
    # all values between the intervals can be calculated due to the principle:
    # 2^(a+b) == 2^a * 2^b
    for x in range(10000,modulo,10000):
        data[x] = reducit(b2[0]*data[x-10000][0],25),lastDigs(b2[1]*data[x-10000][1],25)

    #Lastly calculate the lead 25 digits starting at the modulo and skipping the modulo
    # with each interval. Because we can calculate all the values between the modulo 
    # by combinations of 10k's and 1-10k's, all values less than the maximum 
    # are precalculated. 
    for x in range(modulo,maxi+1,modulo):
        data[x] = reducit(base[0]*data[x-modulo][0],25),lastDigs(base[1]*data[x-modulo][1],25)

    #Evaluate constraints as passed in the input. 
    for i in range(T):
        n,k = cons[i]
        print myFront(n-1,k)+ myEnd(n-1,k)
