
ciphertext = "UONCS VAIHG EPAAH IGIRL BIECS TECSW PNITE TIENO IEEFD OWECX TRSRX STTAR TLODY FSOVN EOECO HENIO DAARQ NAELA FSGNO PTE"

ciphertext= ciphertext.replace(" ","")
total_length = len(ciphertext)

start=0
for i in range(1,total_length+1):
    # different possible way of dimension
    if (total_length % i ==0):
        exp_vowel = (total_length/i)*0.4
        #each row (total: i rows)
        actual_vowel=[0]*i
        #calculate actual num of vowel
        for j in range(total_length):
            if (ciphertext[j]=='A' or ciphertext[j]=='E' or ciphertext[j]=='I' or ciphertext[j]=='O' or ciphertext[j]=='U'):
                actual_vowel[j%i]+=1
        #sum of each row's diff
        sum_diff = 0        
        for k in range(i):
            sum_diff += abs(exp_vowel-actual_vowel[k])
        print(f"For {i} x {total_length/i:.0f} rectangle, the avg of the differences is {sum_diff/i}.")
        


