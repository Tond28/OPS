#inserire la parola nella variabile message (linea 90)
#insert the word in the variable: message (line 90)

#inserire la chiave di crittografia nella variabile message (linea 91)
#insert the word in the variable: message (line 91)

#INSERIRE LA PAROLA IN MAIUSCOLO
#INSERT THE WORD IN CAPS

ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_to_index=dict(zip(ALPHABET, range(len(ALPHABET))))
index_to_letter=dict(zip(range(len(ALPHABET)), ALPHABET))

def encrypt(message, key):
    encrypted=""
    spazi=[]
    mes=""
    enc=""
    counter=0
    for n in range(len(message)):
        if message[n]== " ":
            spazi.append(n)
        else:
            mes=mes+message[n]


    #separa il messaggio nella lunghezza della chiave
    split_message=[mes[i:i + len(key)] for i in range(0, len(mes), len(key))]

    #converte il messaggio in indice e aggiunge la chiave
    for each_split in split_message:
        i=0
    
        for letter in each_split:
                
            number=(letter_to_index[letter]+letter_to_index[key[i]])%len(ALPHABET)
            encrypted+=index_to_letter[number]
            i+=1
    
    for l in range(len(encrypted)+len(spazi)):
        if l in spazi:
            enc=enc+" "
        else:
            enc=enc+encrypted[counter]
            counter+=1
    
    return enc


def decrypt(cipher,key):
    decrypted=""
    spazi=[]
    mes=""
    dec=""
    counter=0
    for n in range(len(cipher)):
        if cipher[n]== " ":
            spazi.append(n)
        else:
            mes=mes+cipher[n]


    #separa il messaggio nella lunghezza della chiave
    split_cipher=[mes[i:i + len(key)] for i in range(0, len(mes), len(key))]

    #converte il cifrario in indece e sottrarre la chiave
    for each_split in split_cipher:
        i=0
    
        for letter in each_split:
            
            number=(letter_to_index[letter]-letter_to_index[key[i]])%len(ALPHABET)
            decrypted+=index_to_letter[number]
                
            i+=1

    for l in range(len(decrypted)+len(spazi)):
        if l in spazi:
            dec=dec+" "
        else:
            dec=dec+decrypted[counter]
            counter+=1
    
    return dec



def main():
    message="WORD"
    key="CLGF"
    scelta=input("Scrivere <criptare> o <decriptare> per selezionare la modalità preferita:  ")
    if scelta=="criptare":
        encrypted_message=encrypt(message, key)
        print(encrypted_message)
    elif scelta=="decriptare":
        decrypted_message=decrypt(message, key)
        print(decrypted_message)



main()

