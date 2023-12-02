from phe import paillier
public_key, private_key = paillier.generate_paillier_keypair(None , 128)
secretNumber1 = 1
secretNumber2 = 1
secretNumber3 = 5
print("Numeros usados:")
print(secretNumber1)
print(secretNumber2)
print(secretNumber3)
print("")
cryptNumber1 = public_key.encrypt(secretNumber1)
cryptNumber2 = public_key.encrypt(secretNumber2)
cryptNumber3 = public_key.encrypt(secretNumber3)

print("Numeros encriptografados:")
print(cryptNumber1.ciphertext())
print(cryptNumber2.ciphertext())
print(cryptNumber3.ciphertext())
print("")


x = cryptNumber1 + cryptNumber2 + cryptNumber3
print("Soma criptografada dos numeros:")
print(x.ciphertext())
print("")

dx = private_key.decrypt(x)
print("Soma descriptografada dos numeros:")
print(dx)