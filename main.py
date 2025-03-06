from utils.encrypt import Encrypt
from utils.decrypt import Decrypt
encrypted = Encrypt("example", 5).encrypt() # encrypting word with shift 5
decrypted_l = Decrypt("jcfruqj").decrypt() # decrypting the encrypted word
decrypted = "".join(i for i in decrypted_l) # converting list to string
print("encrypted:", encrypted, "decrypted:", decrypted)
