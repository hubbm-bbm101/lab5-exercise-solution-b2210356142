a = int(input("bir sayı giriniz"))
listeven = []
listodd = []
for x in range(1, a+1):
    if x%2==0:
        listeven.append(x)
    elif x%2==1:
        listodd.append(x)
print(sum(listodd))
print(sum(listeven)/len(listeven))
