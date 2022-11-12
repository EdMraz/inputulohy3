def vypis_typy(zoznam):
    for i in zoznam:
        if type(i) == str:
            print(i,"- reťazec\n")
        elif type(i) == int or type(i) == float:
            print(i,"- číslo\n")
        else:
            print(i,"- iný typ\n")

vypis_typy([12, 'x', None, 3.14, [], range(5), '123'])
