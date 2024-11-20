import json
import string
alphabet = list(string.ascii_lowercase)
with open("word.json") as file:
    data = json.load(file)

def decrypt(encrypted_word, shift):
    decrypted = ""
    encrypted = encrypted_word.lower().strip()
    encrypted_word = list(encrypted)
    for character in encrypted_word:
        if character in alphabet:
            c_index = alphabet.index(character)
            new_char = alphabet[(c_index - shift) % 26]
            decrypted += new_char
        else:
            decrypted += character
    return decrypted

def main():
    try:
        encrypted_word = input('Please enter the encrypted word: ')
        found_words = []
        for shift in range(26):
            decrypted_word = decrypt(encrypted_word, shift)
            if decrypted_word in data:
                found_words.append(decrypted_word)
                print(f'Found matching word: {decrypted_word} with seed {shift}')

        if not found_words:
            print("No matching words found.")
    except KeyboardInterrupt:
        print('\nexiting')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
