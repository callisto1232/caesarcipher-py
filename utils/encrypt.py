import string 
class Encrypt:
    def __init__(self, word, shift):
        self.word = word
        self.shift = shift
    alphabet = list(string.ascii_lowercase)
    def encrypt(self):
        word = self.word
        shift = self.shift
        alphabet = Encrypt.alphabet
        encrypted = ""
        word = list(word.lower().strip())
        for character in word:
            if character in alphabet:
                c_index = alphabet.index(character)
                new_char = alphabet[(c_index + shift) % 26] 
                encrypted += new_char 
            else:
                encrypted += character
        return encrypted

