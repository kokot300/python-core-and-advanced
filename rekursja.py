def definicja(a=5): #default parameter
    if a == 1:
        return a
    else:
        return a * definicja(a - 1)


x=int(input("number\n"))
abc = definicja(a=x) #mozna zmieniac kolejnosc parametrow np b=10, a=20
print(abc)
