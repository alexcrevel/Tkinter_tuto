from random import shuffle

LANG = ["c", "cpp", "go", "java", "js", "ocaml", 
        "php", "python", "ruby", "scratch"]

print(LANG)

NB_LIG = 4
NB_COL = 5
NB_CARTES = NB_LIG*NB_COL//2
cartes = list(range(NB_CARTES))*2
shuffle(cartes)

P = []
k = 0
for lig in range(NB_LIG):
    L = []
    for col in range(NB_COL):
        L.append(cartes[k])
        k += 1
    P.append(L)

for lig in range(NB_LIG):
    for col in range(NB_COL):
        nro = P[lig][col]
        lang = LANG[nro]
        print(lang, end = " ")
    print()
        