import string 
alphabet = list(string.ascii_lowercase)
def encrypt(word, shift):
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

def main():
    try:
        word = input('what is the word\n')
        shift = int(input('what is the shift\n'))
        print(encrypt(word, shift))
    except ValueError:
        print('you should enter an integer shift value')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
