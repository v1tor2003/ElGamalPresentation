# function to generate key

# generates the group mod integers group (Zp*,x)
def gen(g, p):
    E = []
    # defining empty set
    my_set = set(E)
    for x in range(1, p):
        # generating elements num = g^x mod p
        num = pow(g, x, p)
        my_set.add(num)
    return len(my_set)

# func to get valid inputs in the group interval
def getInputInSet(label):
    while(True):
        result = int(input(label))
        if result >= 1 and result <= (p - 2):
            break

    return result   

# Inverse mod calculator
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0

    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x

print("Receiver side key generation")

p = int(input("Enter a prime number(p): "))

# generating E1

if len(bin(p)) < 129:
    for x in range(1, p):
        if gen(x, p) == (p - 1):
            E1 = x
            break

print("E1 (Generator):", E1)
d = getInputInSet("Enter private key: ")
E2 = pow(E1, d, p)
print("Public key: (", E1, ",", E2, ",", p, ")")
print("Private key(d): ", d)
print(" ")

# Encryption
print("Sender side i.e Alice")
print(" ")
r = getInputInSet("Select a random number (1<r<("+str(p-2)+")): ")
msg = getInputInSet("Enter your msg (1<r<("+str(p-2)+")): ")

C1 = pow(E1, r, p)
C2 = pow((pow(E2, r) * msg), 1, p)

print("Encrypt msg: (", C1,",", C2, ")")
print(" ")

# Decrypt
de_msg = pow((modInverse(pow(C1, d), p) * C2), 1, p)
print("Receiver side decryption: ", de_msg)