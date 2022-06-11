#This is a wordle clone that runs in IDLE IDE.
#I implemented orange and green colors for the letters just like the real game has.

import sys
import random

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

def pickword(wordlist):
    keyword = random.choice(wordlist)
    return keyword

def validguess(wordguess):
    if wordguess in wordlist:
        return True
    return False

def makeguess(guessnum, allkeys):
 
    if guessnum < 7:
        w = input(str(guessnum) + ": ")
        

        if w == 'giveup':
            print ('it was ' + keyword)
            print ('Better luck next time\n')
            main()
        
        if w == 'keys':
            print (allkeys + '\n')
            makeguess(guessnum, allkeys)
        
        outputlist = ''
        if validguess(w):
            index = 0
            DupLetterFix = w
            while index < 5:
                if keyword[index].lower() == DupLetterFix[index]:
                    outputlist += 'G'
                    DupLetterFix = DupLetterFix.replace(keyword[index], '-', 1)
                    
                elif DupLetterFix[index].lower() in keyword:
                       outputlist += 'Y'
                       DupLetterFix = DupLetterFix.replace(DupLetterFix[index], '-', 1)
                else:
                    outputlist += 'N'
                    allkeys = allkeys.replace(w[index].upper(),' ')
  
                index += 1

            for idx in range(len(outputlist)):
                gap = ''
                endline = ''
                if idx == 0:
                    gap = '   '
                elif idx == 4:
                    endline = '\n'
                if outputlist[idx] == 'G':
                    color.write(gap + w[idx] + endline, "STRING")
                elif outputlist[idx] == 'Y':
                    color.write(gap + w[idx] + endline, "KEYWORD")
                else:
                    color.write(gap + w[idx] + endline, "SYNC")
                
            print ('')
            
            if checkcorrect(outputlist):
                print ('WINNER WINNER CHICKEN DINNER \n')
                main()
            else:
                makeguess(guessnum+1, allkeys)
        
        else:
            print ("Not valid \n")
            makeguess(guessnum, allkeys)
    else:
        print ('it was ' + keyword)
        print ('Better luck next time\n')
        main()
        
#("Nah that shit's invalid son")
    
def checkcorrect(outputlist):
    if outputlist == 'GGGGG':
        return True
    else:
        return False
        

def main():

    global wordlist
    wordlist = []
    wordfile = open('wordlewords.txt')
    for line in wordfile:
        line = line.strip()
        wordlist.append(line)

    wordfile.close()

    allkeys = 'Q W E R T Y U I O P\n A S D F G H J K L\n  Z X C V B N M'
    
    global keyword
    keyword = pickword(wordlist)
    
    print ("Welcome to Wordle: Enter a valid 5 letter word.\n\nIf you'd like to see the possible letters remaining, type the word 'keys'\n\nIf you want to give up, type giveup\n")

    guessnum = 1
    makeguess(guessnum, allkeys)
    
main()
