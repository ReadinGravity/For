# Vypočítaj súčet  všetkých  párnych čísiel od 1 do N
n=int(input("zadaj mi ciselko: "))
x=0
for i in range(2,n+1,2):
    x+=i
print(x)
