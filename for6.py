# Naprogramuj funkciu, ktorá v intervale od  <začiatok,  koniec>  zistí počet čísel, ktoré sú deliteľné 8
n=int(input("zaciatok intervalu: "))
x=int(input("konec intervalu: "))
a=0
for i in range(n,x+1):
    if i%8==0:
        a+=1
print(a)
