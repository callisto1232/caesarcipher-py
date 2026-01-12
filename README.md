# caesarcipher-py

## Python script that can both encrypt your messages with Caesar Cipher and decrypt with adjustable shift. 

*"word.json" file is taken from this project: https://github.com/dwyl/english-words*

### Youtube video that I explain this code.

[![A Youtube video that I explain this code.](http://img.youtube.com/vi/NomosMW2T7A/0.jpg)](http://www.youtube.com/watch?v=NomosMW2T7A "Caesar Cipher in Python")

`main.py` file can be used for example. 
```python
from utils.encrypt import Encrypt
from utils.decrypt import Decrypt
shift = 5
encrypt_word = "example"
encrypted = Encrypt(encrypt_word, shift).encrypt() # encrypting word with shift 5
#print("encrypted:", encrypted, "shift:", shift)
decrypted_l = Decrypt(encrypted).decrypt() # decrypting the encrypted word
decrypted = "".join(i for i in decrypted_l) # converting list to string
print("encrypted:", encrypted, "decrypted:", decrypted)

```
# Encryption

In `main.py`, you can change `encrpyt_word` variable and try it with others ``encrypt()`` function is under the class ``Encrypt()`` that is located under utils folder. You can use ``Encrypt("word to be encrypted", shift).encrypt()`` where shift is the number that words letters will be shifted that amount in the alphabet.

*The word example encrypted with shift 5.*
<img width="1032" height="550" alt="image" src="https://github.com/user-attachments/assets/365a8e74-0c6f-438c-8046-bd6e585a0184" />

*The word example encrypted with shift 6.*
<img width="1032" height="550" alt="image" src="https://github.com/user-attachments/assets/9235be32-5426-4856-9297-135c0bac1e5d" />

# Decryption

For decryption, I use a ``word.json`` file that contains all English words. It's some kind of reverse engineering where we try to find the word by substracting number from the encrypted word then searching in word.json to see if there are any matches. And loop this until finding one.

*Encryption of word "example" with shift 5 being decrypted*
<img width="747" height="351" alt="image" src="https://github.com/user-attachments/assets/f3c00b24-411e-4504-9a63-b4ee7cf69420" />
