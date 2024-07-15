
def Count_letter_frequency(ciphertext):
    letter_frequency={}
    total_length=0
    for character in ciphertext:
        if character.isalpha():
            if character in letter_frequency:
                letter_frequency[character]+=1
            else:
                letter_frequency[character]=1
            total_length+=1

    #sort
    sorted_frequency=sorted(letter_frequency.items(), key=lambda c:c[1], reverse=True)
    
    #print
    for letter, frequency in sorted_frequency:
        print(f"{letter}'s frequency: {(frequency/total_length)*100:.2f}%")

ciphertext="C UYGHARMZ IUWMPRWIR GAIR YVRMP MBHMZWMPUM C VMMXWPE YV PYR VCZ ZMGYQMD VZYG CXCZG YP CPCXKTWPE CPD MBHXYZM RNM VXYYD YV CDQCPUMD OPYSXMDEM SNWUN MCUN KMCZ LZWPEI SWRN WR"

Count_letter_frequency(ciphertext)

