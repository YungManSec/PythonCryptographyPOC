import math, time

print("""
             ______ _  _____                       _ 
            |  ____| |/ ____|                     | |
            | |__  | | |  __  __ _ _ __ ___   __ _| |
            |  __| | | | |_ |/ _` | '_ ` _ \ / _` | |
            | |____| | |__| | (_| | | | | | | (_| | |
            |______|_|\_____|\__,_|_| |_| |_|\__,_|_|
                                                        """)

print("Elgamal Encrypt/Decrypt")
print("")
print("Use numbers only in the following prompts")
print("")
print("[+] Creating Private Key!")
p = int(input("    Enter your first prime number (p): "))

g = int(input("    Enter your second prime number (g): "))

x = int(input("    Enter your random x: "))
print("")
y = ((g ** x) % p)
print("    y = ((g ** x) % p)")
print("    Your y value is equal to: " + str(y))
print("")
print("    Your public key is equivalent to: y = " + str(y) + ", g = " + str(g) + ", p = " + str(p))
print("")
print("[+] Encrypting Message Using Public Key!")

m = int(input("    Enter the message you wish to encrypt: "))

r = int(input("    Enter your random r: "))

k = ((y ** r) % p)
print("    Your k is equal to: " + str(k))
print("")

c1 = ((g ** r) % p)
print("    Your C1 is: " + str(c1))

c2 = ((m * k) % p)
print("    Your C2 is: " + str(c2))

kneg = pow(k, p-2, p)
print("    Your inverse modulo k is: " + str(kneg))

print("[+] Decrpyting Message!")
        
time.sleep(2)

m2 = ((kneg * c2) % p)

print("    Your entered decrypted message was: " + str(m))
print("")
print("    Your C1 = " + str(c1))
print("")
print("    Your C2 = " + str(c2))
print("")
print("    Your decrypted message is: " + str(m2))
