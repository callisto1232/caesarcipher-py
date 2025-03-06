import json
import string
class Decrypt:
    alphabet = list(string.ascii_lowercase)
    with open("utils/word.json") as file:
        data = json.load(file)
    def __init__(self, encrypted):
        self.encrypted = encrypted
    def decrypt(self):
        encrypted = self.encrypted
        data = self.data
        alphabet = self.alphabet
        found_words = []
        self.encrypted = encrypted
        encrypted = encrypted.lower().strip()
        encrypted_word = list(encrypted)
        for shift in range(26):
            decrypted = ""
            for character in encrypted_word:
                if character in self.alphabet:
                    c_index = alphabet.index(character)
                    new_char = alphabet[(c_index - shift) % 26]
                    decrypted += new_char
                else:
                    decrypted += character
            if decrypted in data:
                found_words.append(decrypted)
        return found_words

