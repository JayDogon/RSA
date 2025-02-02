import math

primes = []
bprimes = []
def mod(n, a):
    A = n
    terms = [0,1]
    while n != 1 and a !=1:
        if n>a:
            terms.append(n//a)
            n = n%a
        else:
            terms.append(a//n)
            a = a%n
    inv = terms[1]
    inV = terms[0]
    k = 2
    while k <len(terms):
        inv, inV = inV - (terms[k]*inv), inv
        k+=1
    return inv%A
    

c = 2
t = 116
def primer(t, C):
    new = []
    while C<100*t:
        prime = True
        k = 0
        sq = C**0.5
        while k<len(primes):
            if C%primes[k] == 0:
                prime = False
            k+=1
            if k>sq:
                break
        if prime:
            primes.append(C)
            new.append(C)
            if C>11358:
                bprimes.append(C)
        C+=1
    return (C, new)
	
c, ignore = primer(t,c)

print("To begin, pick two distinct primes from this list and enter them separated by a space. If you'd like bigger primes enter \"more primes\".")
print(bprimes)
vinp = False
while vinp is False:
    command = input("Input: ")
    if command == "more primes":
        print ("Coming up.")
        t+=2
        c, new = primer(t,c)
        print(new)
    else:
        B = False
        commands = command.split(" ")
        if len(commands) <2:
            print("Too few inputs.")
        elif len(commands) >2:
            print("Too many inputs.")
        elif (not commands[0].isnumeric) or (not commands[1].isnumeric()):
            try:
                p = float(commands[0])
                q = float(commands[1])
                print("Please enter whole numbers.")
            except:
                print("Please enter numbers or ask for more primes.")
        else:
            p = int(commands[0])
            q = int(commands[1])
            if (p not in bprimes) or (q not in bprimes):
                print("Please pick from the list.")
            elif p == q:
                print("Please pick distinct primes.")
            else:
                vinp = True
                
n = p*q
phi = (p-1)*(q-1)
print("Your \"n\" value is " + str(n) + " and its totient (often called phi) is " + str(phi) +  ".")
print("You'll now need to choose an \"e\" value. This number needs to be coprime to " + str(phi) + ", which is to say they have no common factors other than 1.")
es = []
for x in range (2, phi):
    if math.gcd(x,phi) == 1:
        es.append(x)
    if len(es) == 100:
        break
print("Here's a list to choose from.")
print(es)
vinp = False
while not vinp:
    command = input("Input: ")
    if not command.isnumeric():
        print("Please pick an item from the list.")
    else:
        e = int(command)
        if e not in es:
            print("Please pick an item from the list.")
        else:
            vinp = True
            
            
d = mod(phi, e)
print("Ok, we'll just need one more number, your private key \"d\".")
print("d is " + str(d))
print("Enter \"values\" to see the values of n and e again or \"quit\" to terminate the program.")


def modde(m, dee, en):
    x = str(bin(dee)).lstrip("0b")
    x = x[::-1]
    b = []
    for i in range(0, len(x)):
        b.append(int(x[i]))
    sq = [m]
    for i in range(1, len(x)):
        sq.append((sq[i-1]**2)%en)
    cu = 1
    for i in range(0,len(x)):
        if b[i] == 1:
            cu = (cu*sq[i])%en
        
    #M = m
    #for i in range(0,dee -1):
    #    M = (M*m)%en
    return cu



vinp = False
while vinp is False:
    command = input("Input: ")
    if command == "quit":
        exit()
    elif command == "values":
        print("n is " + str(n) + " and e is " + str(e) + ".")
    elif command[0]!= "[" or command[-1]!= "]":
        print("Invalid input")
    else:
        command = command.lstrip("[")
        command = command.rstrip("]")
        seq = command.split(", ")
        out = ""
        succ = True
        for x in seq:
            if not x.isnumeric() or int(x)>=n:
                print("Invalid list")
                succ = False
                break
            else:
                N = modde(int(x),d,n)
                N = str(N)
                while len(N)!=9:
                    N = "0" + N
                a = int(N[0:3])
                b = int(N[3:6])
                g = int(N[6:9])
                thr = [a,b,g]
                for i in thr:
                    if i>128:
                        print("Invalid sequence")
                        succ = False
                        break
                    else:
                        out += chr(i)
        if succ:
            print(out)
                
            
        
    



