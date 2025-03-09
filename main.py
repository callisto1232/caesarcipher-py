from utils.encrypt import Encrypt
from utils.decrypt import Decrypt
encrypted = Encrypt("example", 5).encrypt()
decrypted_l = Decrypt("jcfruqj").decrypt()
decrypted = "".join(i for i in decrypted_l)
print("encrypted:", encrypted, "decrypted:", decrypted_l)
