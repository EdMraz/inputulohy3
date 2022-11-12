def sucin(zoznam):
    v = 1
    for i in range(0,len(zoznam)):
        v *= zoznam[i]
    return v

print(sucin([2] * 20))
