inizio=[2,8] #x, y
direzione_i="W"
direzioni=["N", "E", "S", "W"]
direzione= direzione_i
comandi=["o","f","f","o","f","f","o","f","f"]
fine=[]
fine.append(inizio[0])
fine.append(inizio[1])
for e in comandi:
    if e =="o":
        if direzione == "W":
            direzione="N"
        else:
            direzione=direzioni[direzioni.index(direzione)+1]
    elif e =="a":
        if direzione == "N":
            direzione="W"
        else:
            direzione=direzioni[direzioni.index(direzione)-1]
    elif e =="f":
        if direzione=="N":
            fine[1]+=1
        elif direzione=="S":
            fine[1]-=1
        elif direzione=="E":
            fine[0]+=1
        elif direzione=="O":
            fine[0]-=1

print("posizione Iniziale:{}\nDirezione Iniziale:{}\nPosizione Finale:{}\nDirezione Finale:{}".format(inizio, direzione_i, fine, direzione))
print("\n\n")
