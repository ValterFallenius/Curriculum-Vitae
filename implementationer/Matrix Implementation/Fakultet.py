def fakultet(n):
    '''Returns n-factorial'''
    fak=1
    for i in range(1,n+1):
        fak*=i
    return fak

#Some testing:
assert fakultet(0)==1
assert fakultet(1)==1
assert fakultet(2)==2
assert fakultet(3)==6
assert fakultet(100)==93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

#Some more testing using math library:
import math

assert fakultet(10000)==math.factorial(10000)
