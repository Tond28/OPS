from itertools import combinations

out={}

ripetizioni = int(input("numero dati da inserire: "))

for i in range(ripetizioni):
    name_dato=input("Nome dato ")
    dati=[]
    first_value=int(input("guadagno "))
    second_value=int(input("peso "))
    dati.append(first_value)
    dati.append(second_value)
    out[name_dato]=dati

print(out , "\n\n")
max_weight=int(input("Inserire peso massimo "))
i = []
k=ripetizioni
list_j=[] 
value_list=[]

out2={}
for e in range (len(out)):
    values=out.keys()
    p=e+1
    com=list(combinations(values, p))
    for name in com:
        value_list.append(name)
counter=0
for t in value_list:
    names=[]
    value=[]
    costo=0
    peso=0
    counter+=1
    for l in t:
        names.append(l)
        costo+=out[l][0]
        peso+=out[l][1]
    if peso <= max_weight:
        value.append(names)
        value.append(costo)
        value.append(peso)
        pos="possibilità "+str(counter)
        out2[pos]=value


for y in out2:
    print("I tag sono: {}, valore: {}, peso: {}".format(out2[y][0], out2[y][1], out2[y][2]))