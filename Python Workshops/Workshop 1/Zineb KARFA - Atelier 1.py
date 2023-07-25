#Exo 1
def puissance (X,n):
    r=1
    for i in range(n):
        r *= X
    return r

#Exo 2
def factorielle (n):
    if(n>0):
        F=1
        for i in range (1,n+1):
            F *= i
        return F
    return 1

#Exo 3
def sommeserie (n):
    if(n <= 0):
        return "le nombre doit etre strictement positif"
    else:
        sum = 0
        for i in range (1,n+1):
            sum = 0
        for i in range (1,n+1):
            sum += factorielle (i-1)
        return sum

#Exo 4
def decimalbinaire (n):
    if n == 0:
        return 0
    else:
        resultat = ""
        while(n > 0):
            r = n%2
            resultat = str(r)+resultat
            n//=2
        return int(resultat)

#Exo 5
def sommenombres(n):
    somme = 0
    for i in range (1,n+1):
        somme += i
    return somme

#Exo 6
def chiffrenombre(n):
    if n == 0:
        return 1
    else:
        CN = 0
        while (n>0):
            CN += 1
            n//=10
        return CN

#Exo 7
def frequencecaractere (str1, char):
    frequence = 0
    for i in str1:
        if(i == char):
            frequence += 1
        return frequence

#Exo 9
## Fonction qui envoie la valeur moyenne d’une liste
def moyenne (list):
    somme = 0
    for i in list:
        somme += i
    return somme / len(list)
