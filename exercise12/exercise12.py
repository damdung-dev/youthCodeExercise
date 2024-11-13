import random

thamsohe=[]

def process(d,dx,dy):
    if d!=0:
        print ("hệ pt có 1 nghiệm duy nhất")
        print("x1 = "+str(dx/d))
        print("y = "+str(dy/d))
    elif d==0 and dx==0 and dy==0:
        print("hpt có vô số nghiệm")
    elif dx!=0 or dy!=0:
        print("hpt vô nghiệm")
    else:
        print("error")

def solve():
    phantu=["a1","a2","b1","b2","c1","c2"]
    for i in range(0,6):
        phantu1=float(input(phantu[i]+"="))
        #phantu1=random.randrange(0,30)
        thamsohe.insert(i,phantu1)
        #print(phantu[i]+"="+str(phantu1))
    d=thamsohe[0]*thamsohe[3]-thamsohe[1]*thamsohe[2]
    dx=thamsohe[4]*thamsohe[3]-thamsohe[5]*thamsohe[2]
    dy=thamsohe[0]*thamsohe[5]-thamsohe[1]*thamsohe[4]
    process(d,dx,dy)

solve()