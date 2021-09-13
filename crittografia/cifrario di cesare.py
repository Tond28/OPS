#inserire la parola nella variabile message (linea 46)
#insert the word in the variable: message (line 46)

#INSERIRE LA PAROLA IN MAIUSCOLO
#INSERT THE WORD IN CAPS

ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_to_index=dict(zip(ALPHABET, range(len(ALPHABET))))
index_to_letter=dict(zip(range(len(ALPHABET)), ALPHABET))

def encrypt(message, shift):
    cipher=""

    for letter in message:
        if letter== " ":
            shifted_letter=letter
        else:
            index=(letter_to_index[letter]+shift)%len(ALPHABET)
            shifted_letter=index_to_letter[index]

        cipher+=shifted_letter

    return cipher


def decrypt(ciphered_text, shift):
    decrypted=""

    for letter in ciphered_text:
        if letter== " ":
            shifted_letter=letter
        else:
            index=(letter_to_index[letter]-shift)%len(ALPHABET)
            shifted_letter=index_to_letter[index]

        decrypted+=shifted_letter

    return decrypted


    
def main():
    #INSERIRE LA PAROLA IN MAIUSCOLO
    #INSERT THE WORD IN CAPS
    message="WORD"
    scelta=input("Scrivere <criptare> o <decriptare> per selezionare la modalità di esecuzione del programma:  ")
    if scelta=="criptare":
        encrypted_message=encrypt(message, 5)
        print(encrypted_message)
    elif scelta=="decriptare":
        decrypted_message=decrypt(message, 2)
        print(decrypted_message)



main()