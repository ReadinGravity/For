# naprogramuj funkciu, ktorá vráti počet všetkych párnych čísel od 1-N
n=int(input("zadaj mi ciselko: "))
x=0
for i in range(2,n+1,2):
    x+=1
print(x)
