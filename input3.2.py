def nakup(zoznam):
    vysledok=0
    for i in range(0,len(zoznam),2):
        vysledok+=zoznam[i]*zoznam[i+1]
    return vysledok

print(nakup([3, 2.5, 0.5, 10, 1.2, 1.2]))
