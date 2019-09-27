#fractions with recurring patterns
N=1000
def recurring_length(subject):
    for i in range(len(subject)):
        temp=subject[0:i+1]
        if temp==subject[i+1:2*i+2]: #and temp==subject[2*i+2:3*i+3]
            return len(temp)

def popfirst(number):
    first=int(str(number)[0])
    number = (number-first)*10
    return (number,first)
number = 1/7
first=0
for i in range(100):
    (number, first)=popfirst(number)
    print(first)

'''
#find highest recurring pattern under N
longest=0
for i in range(2,N+1):
    subject = str(1/i)[2:]
    print(subject)
    length=recurring_length(subject)
    print(length)
    if longest<length:
        longest=length
print(longest)
'''
