alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_to_index=dict(zip(alphabet, range(len(alphabet))))
index_to_letter=dict(zip(range(len(alphabet)), alphabet))

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

    #convertire il messaggio in indice e aggiungere la chiave
    for each_split in split_message:
        i=0
    
        for letter in each_split:
                
            number=(letter_to_index[letter]+letter_to_index[key[i]])%len(alphabet)
            encrypted+=index_to_letter[number]
            i+=1
    print(spazi)
    for l in range(len(encrypted)+len(spazi)):
        if l in spazi:
            enc=enc+" "
        else:
            enc=enc+encrypted[counter]
            counter+=1
    
    return enc


def decrypt(cipher,key):
    decrypted=""

    #separa il messaggio nella lunghezza della chiave
    split_cipher=[cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))]

    #convertire il cifrario in indece e sottrarre la chiave
    for each_split in split_cipher:
        i=0
    
        for letter in each_split:
            
            number=(letter_to_index[letter]+letter_to_index[key[i]]%len(alphabet))
            decrypted+=index_to_letter[number]
                
            i+=1
    
    return decrypted



def main():
    message="APPUNTAMENTO ALLE CINQUE"
    key="CLGF"
    scelta=input("Scrivere <criptare> o <decriptare> per selezionare la modalità preferita:  ")
    if scelta=="criptare":
        encrypted_message=encrypt(message, key)
        print(encrypted_message)
    elif scelta=="decriptare":
        decrypted_message=decrypt(message, key)
        print(decrypted_message)



main()

