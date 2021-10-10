import random
import math

def threecoins():
    l = []
    i = 0
    while i < 100:
        t = random.random()
        m = random.random()
        if t <= 0.7:
            if m <= 0.3:
                l.append(1)
            else:
                l.append(0)
        else:
            if m <= 0.6:
                l.append(1)
            else:
                l.append(0)
        i += 1
    print(l)
    return l



def EM(l):
    a1 = 0.66
    p1 = 0.34
    q1 = 0.56
    flag = 0
    print(sum(l))
    while (flag < 100):
        m = n = 0
        for i in range(len(l)):
            u = a1*(p1**l[i])*((1-p1))**(1-l[i])/(a1*(p1**l[i])*((1-p1))**(1-l[i])+(1-a1)*(q1**l[i])*((1-q1))**(1-l[i]))
            #print(u)
            m += u
            n += u*l[i]
        a1 = m/100
        #print(m)
        p1 = n/m
        q1 = (sum(l)-n)/(100-m)
        flag += 1
        print(a1,p1,q1)
    return a1, p1, q1


print(EM(threecoins()))



