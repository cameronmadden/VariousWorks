#  File: TestCipher.py

#  Description: This program works with cyptography and ciphers.
    #It can decript and encrypt code in various ways through substitution and
    #transposition.

#  Student's Name: Cameron Madden

#  Student's UT EID: crm5224

#  Course Name: CS 313E 

#  Unique Number: 52590

#  Date Created: 9/12/21

#  Date Last Modified: 9/13/21

import sys

def rail_fence_encode ( strng, key ):
    k = 0
    encodeList = []
    while k < int(key):
        encodeList.append(str())
        k+=1
    n = 0
    i = 0
    while i < len(strng):
        while n < key:
            encodeList[n]+=(strng[i])
            i+=1
            if i == len(strng):
                break
            n+=1
        n -= 2
        while n > 0:
            encodeList[n]+=(strng[i])
            i+=1
            if i == len(strng):
                break
            n-=1
        n = 0
    resStr = str()
    j = 0
    while j < len(encodeList):
        resStr += encodeList[j]
        j+=1
    return resStr

def rail_fence_decode ( strng, key ):
    k = 0
    decodeList = []
    while k < int(key):
        decodeList.append(['*']*len(strng)) #Creates (key) lists of length(strng) filled with *s
        k+=1
    n = 0
    i = 0
    while i < len(strng):
        while n < key:
            decodeList[n][i] = ''
            i+=1
            if i == len(strng):
                break
            n+=1
        n -= 2
        while n > 0:
            decodeList[n][i] = ''
            i+=1
            if i == len(strng):
                break
            n-=1
        n = 0
    n = 0
    #The following triple for loop replaces the ''s with the letters in strng
    for x in range(len(strng)):
        for y in range(len(decodeList)):
            for z in range(len(decodeList[y])):
                if decodeList[y][z] == '':
                    decodeList[y][z] = strng[x]
                else:
                    continue
                x+=1
    
    resStr = str()
    q = 0
    #iterates right to left through the 2D list, if the list was presented in matrix form.
    while q < len(strng):
        for r in range(len(decodeList)):
            if decodeList[r][q] == '*':
                None
            else:
                resStr += decodeList[r][q]
        q+=1
        
    return resStr


def filter_string ( strng ):
    i=0
    resStrng = str()
    while i < len(strng):
        if 97 <= ord(strng[i]) <= 122:
            resStrng += strng[i]
        elif 65 <= ord(strng[i]) <= 90:
            resStrng += chr(ord(strng[i])+32)
        else:
            resStrng += ''
        i+=1
    return resStrng
    
def encode_character (p, s):
    vigList = ['abcdefghijklmnopqrstuvwxyz','bcdefghijklmnopqrstuvwxyza','cdefghijklmnopqrstuvwxyzab','defghijklmnopqrstuvwxyzabc','efghijklmnopqrstuvwxyzabcd','fghijklmnopqrstuvwxyzabcde','ghijklmnopqrstuvwxyzabcdef',
               'hijklmnopqrstuvwxyzabcdefg','ijklmnopqrstuvwxyzabcdefgh','jklmnopqrstuvwxyzabcdefghi','klmnopqrstuvwxyzabcdefghij','lmnopqrstuvwxyzabcdefghijk','mnopqrstuvwxyzabcdefghijkl','nopqrstuvwxyzabcdefghijklm',
               'opqrstuvwxyzabcdefghijklmn','pqrstuvwxyzabcdefghijklmno','qrstuvwxyzabcdefghijklmnop','rstuvwxyzabcdefghijklmnopq','stuvwxyzabcdefghijklmnopqr','tuvwxyzabcdefghijklmnopqrs','uvwxyzabcdefghijklmnopqrst',
               'vwxyzabcdefghijklmnopqrstu','wxyzabcdefghijklmnopqrstuv','xyzabcdefghijklmnopqrstuvw','yzabcdefghijklmnopqrstuvwx','zabcdefghijklmnopqrstuvwxy']
    alphabetStr= 'abcdefghijklmnopqrstuvwxyz'
    decode = str(s)
    pos = alphabetStr.find(p)
    pos2 = alphabetStr.find(s)
    result = vigList[pos][pos2]
    return result

def decode_character (p, s):
    vigList = ['abcdefghijklmnopqrstuvwxyz','bcdefghijklmnopqrstuvwxyza','cdefghijklmnopqrstuvwxyzab','defghijklmnopqrstuvwxyzabc','efghijklmnopqrstuvwxyzabcd','fghijklmnopqrstuvwxyzabcde','ghijklmnopqrstuvwxyzabcdef',
               'hijklmnopqrstuvwxyzabcdefg','ijklmnopqrstuvwxyzabcdefgh','jklmnopqrstuvwxyzabcdefghi','klmnopqrstuvwxyzabcdefghij','lmnopqrstuvwxyzabcdefghijk','mnopqrstuvwxyzabcdefghijkl','nopqrstuvwxyzabcdefghijklm',
               'opqrstuvwxyzabcdefghijklmn','pqrstuvwxyzabcdefghijklmno','qrstuvwxyzabcdefghijklmnop','rstuvwxyzabcdefghijklmnopq','stuvwxyzabcdefghijklmnopqr','tuvwxyzabcdefghijklmnopqrs','uvwxyzabcdefghijklmnopqrst',
               'vwxyzabcdefghijklmnopqrstu','wxyzabcdefghijklmnopqrstuv','xyzabcdefghijklmnopqrstuvw','yzabcdefghijklmnopqrstuvwx','zabcdefghijklmnopqrstuvwxy']
    alphabetStr= 'abcdefghijklmnopqrstuvwxyz'
    s = str(s)
    p = str(p)
    pos = alphabetStr.find(p) 
    letterpos = vigList[pos].find(s)
    result = alphabetStr[letterpos]
    return result 


def vigenere_encode ( strng, phrase ):
    vigList = ['abcdefghijklmnopqrstuvwxyz','bcdefghijklmnopqrstuvwxyza','cdefghijklmnopqrstuvwxyzab','defghijklmnopqrstuvwxyzabc','efghijklmnopqrstuvwxyzabcd','fghijklmnopqrstuvwxyzabcde','ghijklmnopqrstuvwxyzabcdef',
               'hijklmnopqrstuvwxyzabcdefg','ijklmnopqrstuvwxyzabcdefgh','jklmnopqrstuvwxyzabcdefghi','klmnopqrstuvwxyzabcdefghij','lmnopqrstuvwxyzabcdefghijk','mnopqrstuvwxyzabcdefghijkl','nopqrstuvwxyzabcdefghijklm',
               'opqrstuvwxyzabcdefghijklmn','pqrstuvwxyzabcdefghijklmno','qrstuvwxyzabcdefghijklmnop','rstuvwxyzabcdefghijklmnopq','stuvwxyzabcdefghijklmnopqr','tuvwxyzabcdefghijklmnopqrs','uvwxyzabcdefghijklmnopqrst',
               'vwxyzabcdefghijklmnopqrstu','wxyzabcdefghijklmnopqrstuv','xyzabcdefghijklmnopqrstuvw','yzabcdefghijklmnopqrstuvwx','zabcdefghijklmnopqrstuvwxy']
    alphabetStr= 'abcdefghijklmnopqrstuvwxyz'
    phrase = str(phrase)
    result = str()
    j = 0
    #if the phrase is shorter than the string, this function loops the phrase.
    if len(phrase) < len(strng):
        while len(phrase) < len(strng):
            phrase = phrase + phrase
        amtRemoved = len(phrase)-len(strng)
        k = 1
        while k <= amtRemoved:
            phrase.replace(phrase[-k],"")
            k+=1
        
    for i in range(len(strng)):
        pos = alphabetStr.find(strng[i])
        pos2 = alphabetStr.find(phrase[j])
        result += vigList[pos][pos2]
        j+=1
    return result


def vigenere_decode ( strng, phrase ):
    vigList = ['abcdefghijklmnopqrstuvwxyz','bcdefghijklmnopqrstuvwxyza','cdefghijklmnopqrstuvwxyzab','defghijklmnopqrstuvwxyzabc','efghijklmnopqrstuvwxyzabcd','fghijklmnopqrstuvwxyzabcde','ghijklmnopqrstuvwxyzabcdef',
               'hijklmnopqrstuvwxyzabcdefg','ijklmnopqrstuvwxyzabcdefgh','jklmnopqrstuvwxyzabcdefghi','klmnopqrstuvwxyzabcdefghij','lmnopqrstuvwxyzabcdefghijk','mnopqrstuvwxyzabcdefghijkl','nopqrstuvwxyzabcdefghijklm',
               'opqrstuvwxyzabcdefghijklmn','pqrstuvwxyzabcdefghijklmno','qrstuvwxyzabcdefghijklmnop','rstuvwxyzabcdefghijklmnopq','stuvwxyzabcdefghijklmnopqr','tuvwxyzabcdefghijklmnopqrs','uvwxyzabcdefghijklmnopqrst',
               'vwxyzabcdefghijklmnopqrstu','wxyzabcdefghijklmnopqrstuv','xyzabcdefghijklmnopqrstuvw','yzabcdefghijklmnopqrstuvwx','zabcdefghijklmnopqrstuvwxy']
    alphabetStr= 'abcdefghijklmnopqrstuvwxyz'
    phrase = str(phrase)
    result = str()
    j = 0
    if len(phrase) < len(strng):
        while len(phrase) < len(strng):
            phrase = phrase + phrase
        amtRemoved = len(phrase)-len(strng)
        k = 1
        while k <= amtRemoved:
            phrase.replace(phrase[-k],"")
            k+=1
        
    for i in range(len(strng)):
        pos = alphabetStr.find(phrase[j]) 
        letter = vigList[pos].find(strng[i])
        result += alphabetStr[letter]
        j+=1
    return result

def main():
    line1 = sys.stdin.readline()
    line1 = line1.strip()
    RFencode = str(line1)
    
    line2 = sys.stdin.readline()
    RFEkey = int(line2)
    
    eText = rail_fence_encode ( RFencode, RFEkey )
    print ("Rail Fence Cipher")
    print ("")
    print ("Plain Text:", RFencode)
    print ("Key:", RFEkey)
    print ("Encoded Text:", eText)

    line3 = sys.stdin.readline()
    line3 = line3.strip()
    RFdecode = str(line3)

    line4 = sys.stdin.readline()
    RFDkey = int(line4)

    dText = rail_fence_decode ( RFdecode, RFDkey )
    print ("")
    print ("Encoded Text:", RFdecode)
    print ("Key:", RFDkey)
    print ("Decoded Text:", dText)
    print ("")

    line5 = sys.stdin.readline()
    line5 = line5.strip()
    Vencode = str(line5)

    line6 = sys.stdin.readline()
    line6 = line6.strip()
    Phencode = str(line6)

    VeText = vigenere_encode ( Vencode, Phencode )
    print ("Vigenere Cipher")
    print ("")
    print ("Plain Text:", Vencode)
    print ("Pass Phrase:", Phencode)
    print ("Encoded Text:", VeText)

    line7 = sys.stdin.readline()
    line7 = line7.strip()
    Vdecode = str(line7)

    line8 = sys.stdin.readline()
    line8 = line8.strip()
    Phdecode = str(line8)

    VdText = vigenere_decode ( Vdecode, Phdecode )
    print ("")
    print ("Encoded Text:", Vdecode)
    print ("Pass Phrase:", Phdecode)
    print ("Decoded Text:", VdText)
    
if __name__ == "__main__":
  main()
