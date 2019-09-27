powers=[]
for a in range(2,101):
    for b in range(2,101):
        powers.append(a**b)
print(len(powers))
powers.sort()
print(len(powers), "sorted")
temp=0
powers_nodup=[]
for power in powers:
    if power==temp:
        continue
    else:
        powers_nodup.append(power)
        temp=power
print(len(powers_nodup), "no duplicated")
