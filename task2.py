import itertools
from collections import Counter

def monoalphabetic_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = {alphabet[i]: key[i] for i in range(len(alphabet))}
    ciphertext = "".join([mapping[char] if char in mapping else char for char in plaintext.upper()])
    return ciphertext

def monoalphabetic_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reverse_mapping = {key[i]: alphabet[i] for i in range(len(alphabet))}
    plaintext = "".join([reverse_mapping[char] if char in reverse_mapping else char for char in ciphertext.upper()])
    return plaintext

def frequency_analysis(ciphertext):
    frequencies = Counter(ciphertext.replace(" ", ""))
    return frequencies.most_common()

def brute_force_attack(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for perm in itertools.permutations(alphabet):
        key = "".join(perm)
        decrypted_text = monoalphabetic_decrypt(ciphertext, key)
        print(f"Key: {key} -> Decrypted Text: {decrypted_text}")

def generate_playfair_matrix(keyword):
    keyword = "".join(dict.fromkeys(keyword.upper().replace("J", "I")))  # Remove duplicates & J=I
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Exclude 'J'
    for char in keyword:
        alphabet = alphabet.replace(char, "")
    matrix = list(keyword + alphabet)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def print_playfair_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

def main():
    # User Inputs
    key = input("Enter the monoalphabetic cipher key (26 letters): ")
    plaintext = input("Enter the text to encrypt: ")
    ciphertext = monoalphabetic_encrypt(plaintext, key)
    print(f"Encrypted Text: {ciphertext}")
    
    decrypt_choice = input("Do you want to decrypt a text? (yes/no): ").lower()
    if decrypt_choice == "yes":
        ciphertext = input("Enter the text to decrypt: ")
        decrypted_text = monoalphabetic_decrypt(ciphertext, key)
        print(f"Decrypted Text: {decrypted_text}")
    
    # Frequency Analysis
    cipher_text_sample = input("Enter the ciphertext for frequency analysis: ")
    print("Frequency Analysis:", frequency_analysis(cipher_text_sample))
    
    # Playfair Cipher Matrix Generation
    keyword = input("Enter the Playfair cipher keyword: ")
    matrix = generate_playfair_matrix(keyword)
    print("Playfair Matrix:")
    print_playfair_matrix(matrix)

if __name__ == "__main__":
    main()
