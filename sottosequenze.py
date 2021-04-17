from itertools import combinations

sottosequenza = [8,10,11,12,4,18,6,7,14,10,18,20]
num_tot = len(sottosequenza)
sottoseq_possibili_tot = []
sottoseq_possibili = []
sottoseq_lenght = []
sottoseq_valuein = []


def crescente(lista, index_data):
    if not lista[index_data-1] <= lista[index_data]: return True

def strettamente_crescente(lista, index_data):
    if not lista[index_data-1] < lista[index_data]: return True

def decrescente(lista, index_data):
    if not lista[index_data-1] >= lista[index_data]: return True

def strettamente_decrescente(lista, index_data):
    if not lista[index_data-1] > lista[index_data]: return True

def printer(lista):
    for el in lista:
        print(el, end="    ")

def get_sequenze_lun(lenght):
    for e in sottoseq_possibili:
        if len(e)==lenght:
            sottoseq_lenght.append(e)
    sottoseq_lenght.sort()
    return len(sottoseq_lenght)

def calcolo_valore(lista_valori):
    risultato=1 ###################
    for e in lista_valori:
        risultato *= e ##################################
    return risultato




def max_(lista):
    massimo=[lista[0]]
    lista_def=lista
    lista_def.remove(lista_def[0])
    for e in lista_def:
        if calcolo_valore(massimo[0]) == calcolo_valore(e):
            massimo.append(e)
        elif calcolo_valore(massimo[0]) < calcolo_valore(e):
            massimo=[e]
    return massimo

def min_(lista):
    minimo=[lista[0]]
    lista_def=lista
    lista_def.remove(lista_def[0])
    for e in lista_def:
        if calcolo_valore(minimo[0]) == calcolo_valore(e):
            minimo.append(e)
        elif calcolo_valore(minimo[0]) > calcolo_valore(e):
            minimo=[e]
    return minimo

def value_in_list(lista, value, position=404):
    for e in lista:
        if position == 404:
            if value in e:
                sottoseq_valuein.append(e)
        else:
            if e[position]==value:
                sottoseq_valuein.append(e)
    return len(sottoseq_valuein)



for e in range (0, num_tot):
    p=e+1
    com=list(combinations(sottosequenza, p))
    for n in com:
        sottoseq_possibili_tot.append(list(n))

for sot in sottoseq_possibili_tot:
    for data in range(1, len(sot)):
        if crescente(sot, data): #################################
            break
    else:
        sottoseq_possibili.append(sot)
        
    
sottoseq_possibili.sort(key=len)

printer(sottoseq_possibili)
print("\n\n")
get_sequenze_lun(4) #########################sottoseq_lenght
printer(sottoseq_lenght)
print("\n\n")
print("Max_Totale:", max_(sottoseq_lenght), "\n") ###########
print("Min_Totale:", min_(sottoseq_lenght), "\n") ###########
print("\n\n")
value_in_list(sottoseq_lenght, 6, position=0)
printer(sottoseq_valuein)

    
