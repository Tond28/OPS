inizio=[7,20] #x, y
direzione_i="E"
direzioni=["N", "E", "S", "W"]
direzione= direzione_i
comandi=["f","f", "f","f","f","f","f", "o", "f","f", "f","f","f","f","f", "o", "f","f", "f","f","f","f","f", "o"]
fine=[]
posizioni = []
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
        pos=[]
        pos.append(fine[0])
        pos.append(fine[1])
        posizioni.append(pos)
print(posizioni) #elenco spostamenti
for x in range(30): #dimensione mappa
    for y in range(30): #dimensione mappa
        pos=[]
        pos.append(x)
        pos.append(y)
        spaziatura = ""
        spazi = len(str(len(posizioni)+1))
        for i in range (spazi):
            spaziatura = spaziatura + " "
        spaziatura = "[" + spaziatura + "]"
        
        if pos in posizioni:
            if len(str(len(posizioni)+1)) > len(str(posizioni.index(pos)+1)):
                num = str(posizioni.index(pos)+1)
                diff = len(str(len(posizioni)+1))-len(str(posizioni.index(pos)+1))
                for i in range(diff):
                    num = "0" + num
                print("[{}]".format(num), end="")
            else:
                print("[{}]".format(posizioni.index(pos)+1), end="")
        else:

            print(spaziatura, end="")
    print("")

print("posizione Iniziale:{}\nDirezione Iniziale:{}\nPosizione Finale:{}\nDirezione Finale:{}".format(inizio, direzione_i, fine, direzione))
print("\n\n")
