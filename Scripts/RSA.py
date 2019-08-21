# Function Declarations

def egcd(a, b):				# Calculates Euclidian GCD,  return (g, x, y) ...  a*x + b*y = gcd(x, y)
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):			# Calculates Inverse Mod
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
# End of  Function Declarations

print ("Welcome to RSA Encryption Program !!!")
print ("Please provide the following information as Integer !!!");

p_str = input("Enter the value of 'p' (as Integer): ")
p = int (p_str)	# 1st prime number
q_str = input("Enter the value of 'q' (as Integer): ")
q = int (q_str) 	# 2nd prime number
e_str = input("Enter the value of 'e' (as Integer): ")
e = int (e_str)	# Public Key parameter "e"

n = p*q	# Key parameter "n"

print ("The value of 'n' is: "+ str (n))

phi_n = (p-1) * (q-1)	# Function Phi(n) 

print ("The value of 'Phi(n)' is: "+ str (phi_n))

print ("The Public-Key (n,e) := ("+str (n)+", "+str (e)+")");

d = modinv (e, phi_n)	# Private Key parameter "d"

print ("The value of 'd' is: "+ str (d))

print ("The Private-Key (n,d) := ("+str (n)+", "+str (d)+")");

m_str = input("Enter the value of Message 'm' (as Integer): ")
m = int (m_str)		# Input Message

C = pow (m,e,n)	# Encrypted Message

print ("The Ciphertext 'C' is: "+ str (C))

M = pow(C,d,n)		# Decrypted Message

print ("The Decrypted Plaintext 'P' is: "+ str (M))

"""
##############  Output #################

Welcome to RSA Encryption Program !!!
Please provide the following information as Integer !!!
Enter the value of 'p' (as Integer): 3
Enter the value of 'q' (as Integer): 11
Enter the value of 'e' (as Integer): 7
The value of 'n' is: 33
The value of 'Phi(n)' is: 20
The Public-Key (n,e) := (33, 7)
The value of 'd' is: 3
The Private-Key (n,d) := (33, 3)
Enter the value of Message 'm' (as Integer): 2
The Ciphertext 'C' is: 29
The Decrypted Plaintext 'P' is: 2
"""

