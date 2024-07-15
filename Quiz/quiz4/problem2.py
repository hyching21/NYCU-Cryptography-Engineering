# 2-a
key = [0,0,0,0,0,0,0,1]
polynomial = [1,0,0,0,1,1,1,0,1]
plaintext = "ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRANSCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCO\
MPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUETOBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMUCHGREATERTOGETHERTHA\
NWECANINDIVIDUALLYAFTERALLTHATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSITYINTHEFIRSTPLACE"
ciphertext = ""
decrypted_text = ""
cipherchar = []
for i in range(len(plaintext)):
    m = [0]*8
    ct =""
    character = bin(ord(plaintext[i])) # convert to binary representation
    for j in range(2,9):
        m[j-1] = int(character[j])
        
    for j in range(8):
        ciphertext += str(key[j] ^ m[j])
        ct += str(key[j] ^ m[j])
    cipherchar.append(ct)

    #LFSR to generate key stream
    tmp = key[0]
    for j in range(7):
        key[j] = key[j+1] 

    key[7] = 0
    if (tmp == 1):
        for i in range(8):
            key[i] = key [i] ^ polynomial[i+1]

ascii_ciphertext = ""
for i in range(0, len(ciphertext), 8):
    chunk = ciphertext[i:i+8]  # Extract 8-bit chunk

    decimal_value = int(chunk, 2)  # Convert binary to decimal

    ascii_ciphertext += chr(decimal_value)  # Convert decimal to ASCII character


print("ciphertext (ASCII):")
print(ascii_ciphertext)
print("ciphertext:")
print(ciphertext+"\n")

# # decryption
key = [0,0,0,0,0,0,0,1]
for ch in cipherchar:
    pt = ""
    for j in range(8):
        pt += str(key[j] ^ int(ch[j]))
    tmp = key[0]
    for j in range(7):
        key[j] = key[j+1] 
    #LFSR
    key[7] = 0
    if (tmp == 1):
        for i in range(8):
            key[i] = key [i] ^ polynomial[i+1]  
    pt = chr(int(pt,2))
    decrypted_text += pt

print("decrypted text:")
print(decrypted_text)

# # bonus: 2-c
# using the MSB of a0 to a15
a = [0]*16
for i in range(16):
    a[i] = int(cipherchar[i][0])
c = [0]*8


for i in range(255):
    flag = 1
    for j in range(8):
        ac = 0 # the sum of c*a
        for k in range(8):
            ac += c[k] * a[j+1+k]
        if(a[j] != ac%2):
            flag = 0
            break
    if flag == 1:
        c.reverse()
        print(c)
        break
 
    n = 0
    while(c[n]):
        c[n] = 0
        n += 1
    c[n] = 1

