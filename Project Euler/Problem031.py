'''from random import randrange


coins=[200,100,50,20,10,5,2,1]
N=10**10
strands=[]
for i in range(N):
    value=0
    string=""
    while value!=200:
        tempindex=randrange(0,6)
        coin=coins[tempindex]
        if value+coin>200:
            continue
        else:
            value+=coin
            string+=str(tempindex)
    strands.append(string)
strands_nodup = list(dict.fromkeys(strands))
print(len(strands_nodup))

#try 2
import itertools
coins=[200,100,50,20,10,5,2,1]
allcoins=[]
for coin in coins:
    for i in range(int(200/coin)):
        allcoins.append(coin)
indices=list(range(len(allcoins)))

combinations=list(itertools.combinations_with_replacement("012345678",8))
#print(combinations)
twohundredcombs=[]
for comb in combinations:
    value=0
    for item in comb:
        value+=coins[int(item)]
    if value==200:
        twohundredcombs.append(value)
print(len(twohundredcombs))
print(len(combinations))

coins=[200,100,50,20,10,5,2,1]
count=0
for i in range(1):
    for j in range(2):
        for k in range(4):
            for l in range(10):
                for m in range(20):
                    for o in range(40):
                        for p in range(100):
                            for q in range(200):
                                count+=1
print(count)
'''
