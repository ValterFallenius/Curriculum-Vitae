from decimal import *
getcontext().prec=100
def repetition_length(n):
    decimalpoints=str(n)[2:]
    repetition = False
    i=0
    while repetition is not True:
        dec_length=int((len(decimalpoints)-i-1)/2)
        if 0>dec_length:
            return 0
        for j in range(1,dec_length):
            if decimalpoints[i:i+j]==decimalpoints[i+j:i+2*j]==decimalpoints[i+2*j:i+3*j]==decimalpoints[i+3*j:i+4*j]:
                return j
        i+=1

long_length=0
denom=1
for i in range(1,1000):
    temp=repetition_length(Decimal(1)/Decimal(i))
    if long_length<temp:
        long_length=temp
        print(denom)
        denom=i
    elif long_length==temp:
        denom=[denom, i]
print(long_length, denom)
print(len(str(Decimal(1)/Decimal(denom))))
