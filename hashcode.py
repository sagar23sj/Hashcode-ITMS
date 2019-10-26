from random import randrange as rr
from random import random as ra


#P denotes the number of players (in this case, the signals)
P= (1,2)

#S denotes the strategies available to each timer. 
T= int(input())
S= tuple(range(T))


#Defining an inflow and outflow function
def iflo():
    ifl=rr(4,10)
    return ifl
def oflo():
    ofl=rr(4,10)
    return ofl

#Original backlogs
Bklgs= [rr(5,10) for i in range(2)]

#Matching each signal to its backlog
siglog= dict(zip(P,Bklgs))
print(siglog)


#Let us seed the inflow and outflow rates
ifl1= 4
ifl2= 20
ofl1=7
ofl2=2
print(ifl1,ifl2,ofl1,ofl2)

t1= (Bklgs[0]-Bklgs[1]+(ifl1+ofl2)*T)/(ifl1+ifl2+ofl1+ofl2)
t2= (Bklgs[1]-Bklgs[0]+(ifl2+ofl1)*T)/(ifl1+ifl2+ofl1+ofl2)

print(t1,t2)
