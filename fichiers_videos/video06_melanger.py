from random import shuffle

LANG=['c', 'cpp', 'go', 'java', 'js', 'ocaml',
      'php', 'python', 'ruby', 'scratch']

print(LANG)

NB_LIG=4
NB_COL=5
NB_CARTES=NB_LIG*NB_COL//2
print(NB_CARTES)
cartes=list(range(NB_CARTES))*2
print(cartes)

shuffle(cartes)
print(cartes)

plateau=[]
k=0

for lig in range(NB_LIG):
    L=[]
    for col in range(NB_COL):
        L.append(cartes[k])
        k=k+1
    plateau.append(L)
print()
print(plateau)




for lig in range(NB_LIG):
    for col in range(NB_COL):
        nro=plateau[lig][col]
        lang=LANG[nro]
        print(lang, end= " ")
    print()
    print()










        












