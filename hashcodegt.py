from random import randrange as rr
from random import random as ra



#P denotes the number of players (in this case, the signals)
N=float(input("No. of signals: "))
P= tuple(range(N))



#S denotes the strategies available to each timer. 
T= float(input("Circuit length: "))
S= tuple(range(T))



#Original backlogs
JF= float(input("Enter jam factor: "))
Bklgs= [rr(5,10) for i in range(N)]



#Matching each signal to its backlog
siglog= dict(zip(P,Bklgs))
print(siglog)



#Seeding the inflow and outflow rates
ifl=[]
ofl=[]
for i in range(N):
    ifl.append(float(input("Enter inflow rate: ")))
    ofl.append(float(input("Enter outflow rate: ")))

print(ifl,ofl)



times=[]
for i in range(len(Bklgs)):
    t=[]
    for o in Bklgs:
        t.append(o)
    j=Bklgs[i]
    t.pop(i)
    k=[]
    for p in ofl:
        k.append(p)
    k.pop(i)
    time=(j-(sum(t)/len(t))+ifl[i]*T+(sum(k)/len(k))*T)/(sum(ifl)+sum(ofl))
    times.append(time)

print(times)
print(sum(times))
