# Naprogramuj funkciu, ktorá zistí počet všetkých čísel od , ktoré sú deliteľné siedmymi a štyrmi.
n=int(input("zadaj mi ciselko: "))
x=0
for i in range(1,n+1):
    if i%7==0 and i%4==0:
        x+=1
print(x)
