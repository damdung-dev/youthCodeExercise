import random

def bubblesort(list,n):
    for j in range(0,302):
        for i in range(0,299):
            if list[i]>list[i+1]:
                temp=list[i+1]
                list[i+1]=list[i]
                list[i]=temp

list=[]
for i1 in range(0,300):
    number=random.randrange(0,100)
    list.insert(0,number)
bubblesort(list,len(list))
print (list)