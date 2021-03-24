

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_to_index=dict(zip(alphabet, range(len(alphabet))))
index_to_letter=dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, shift):
    cipher=""

    for letter in message:
        if letter== " ":
            shifted_letter=letter
        else:
            index=(letter_to_index[letter]+shift)%len(alphabet)
            shifted_letter=index_to_letter[index]

        cipher+=shifted_letter

    return cipher


def decrypt(ciphered_text, shift):
    decrypted=""

    for letter in ciphered_text:
        if letter== " ":
            shifted_letter=letter
        else:
            index=(letter_to_index[letter]-shift)%len(alphabet)
            shifted_letter=index_to_letter[index]

        decrypted+=shifted_letter

    return decrypted


    
def main():
    message=" "
    scelta=input("Scrivere <criptare> o <decriptare> per selezionare la modalità preferita:  ")
    if scelta=="criptare":
        encrypted_message=encrypt(message, 17)
        print(encrypted_message)
    elif scelta=="decriptare":
        decrypted_message=decrypt(message, 2)
        print(decrypted_message)



main()