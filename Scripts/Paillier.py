import math, time

restart = "y"

while str(restart != "n" or "N"):
    def egcd(a, b):				
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = egcd(b % a, a)
            return (g, y - (b // a) * x, x)
        
    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    print("""
                     /$$$$$$$            /$$ /$$ /$$ /$$                    
                    | $$__  $$          |__/| $$| $$|__/                    
                    | $$  \ $$  /$$$$$$  /$$| $$| $$ /$$  /$$$$$$   /$$$$$$ 
                    | $$$$$$$/ |____  $$| $$| $$| $$| $$ /$$__  $$ /$$__  $$
                    | $$____/   /$$$$$$$| $$| $$| $$| $$| $$$$$$$$| $$  \__/
                    | $$       /$$__  $$| $$| $$| $$| $$| $$_____/| $$      
                    | $$      |  $$$$$$$| $$| $$| $$| $$|  $$$$$$$| $$      
                    |__/       \_______/|__/|__/|__/|__/ \_______/|__/
                                                                            """)
                                                            
    print("Paillier Encrypt/Decrypt")
    print("")
    print("Use numbers only in the following prompts")
    print("")
    print("[+] Creating Public Key!")
    p = int(input("    Enter your first prime number (p): "))
    q = int(input("    Enter your second prime number (q): "))
    g = int(input("    Enter your random g: "))
    print("")
    n = (p * q)
    print("    Your public key is equivalent to: n = " + str(n) + ", g = " + str(g))
    print("")
    print("[+] Creating Private Key and Encrypting Message Using Public Key!")
    m = int(input("    Enter the message you wish to encrypt: "))

    r = int(input("    Enter your random r: "))
    def lcmMinusOne(p, q):
        return abs((p - 1) * (q - 1)) // math.gcd((p - 1), (q - 1))
    lamda = lcmMinusOne(p, q)
    print("    Your λ is equal to: " + str(lamda))
    a1 = (g ** lamda)
    k = ((a1 % (n ** 2)) - 1)/(n)
    print("    Your k is equal to: " + str(k))
    u = modinv(k, n)
    print("    Your u is equal to: " + str(u))
    print("")
    print("    Your private key is equivalent to: λ = " + str(lamda) + ", u = " + str(u))
    c = (((g ** m)*(r ** n)) % (n ** 2))
    print("    Your C is: " + str(c))
    print("")
    print("[+] Decrpyting Message!")
    m2 = ((((((c ** lamda)%(n ** 2)) - 1)/(n))*(u))%(n))
    print("    Your entered decrypted message was: " + str(m))
    print("")
    print("    Your C is = " + str(c))
    print("""
            ░▄▄▄▄░▄▄█▀▀▀███▀▀▀▀▀▀█▄░░░░
            ░░▄█▀██▄░░░░░░▀█░░░░░▄░█▄▄▄
            ░▄█░░░░░██░░░░░▀▀░▄▄██▀▀▀▄░
            ▄█░░▄▄▄▄▄█▀░░░░░░██▀░▄▄▄▄▀▄
            ██░█▀▀▀█▀▀█░░░░░░░░▄█▄▄▄█▄█
            ▀█░▀█▀▀▀██▀░░░░░░░█░░█▄░▄██
            ░█░░░▀▀▀▀░░░░░░░░░█▀▀▀▀██░█
            ░█▄░░░░░░░░░░░░░░░░▀▀▀▀▀░▄█
            ░▀█░░░░░█▀█▄░░▀▀▀░░▄▄▄░░░██
            ░░▀█▄░░░▀▄░▀█░░░▄▄▀▀░█░░▄░█
            ░░░▀██▄░░▀▄░░█▄█▀░▄▄██░░▀█░
            ░░░░░█▀▀░░▀█░░░░░▀░░▄█▄░▄▀░
            ░░░░░░░░░░░░░░░░░░░░▀░█░░░░.
                                 """)
    time.sleep(2)
    print("    Your decrypted message is: " + str(int(m2)))
    restart = str(input("[+] Would you like to restart? (Y / Ctrl + C): "))    
print("[+] Good bye!")
time.sleep(5)
        

