lists=[[1]]
n=1
for i in range(500):

    for j in range(4):
        temp=[]
        for k in range(2+2*i):
            n+=1
            temp.append(n)
        lists.append(temp)

sumation=0
for list in lists:
    sumation+=list[-1]
print(sumation)
