import random
szam = 0
count = 0
rsz = 0
while szam < 20:
    rsz = random.randint (1,12)
    if rsz %3 == 0:
        print(rsz)
        count += 1
    szam += 1
print('Ennyi szám osztható hárommal: '+ str (count))