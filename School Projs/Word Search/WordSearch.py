#  File: WordSearch.py

#  Description: This program takes a word search along with a list of words to find as an input and outputs the coordinates of the first
    #letter of each given word in the word search.

#  Student Name: Cameron Madden

#  Student UT EID: crm5224

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E 

#  Unique Number: 52590

#  Date Created: 9/1/21

#  Date Last Modified: 9/3/21

import sys

wordSearchList = []
wordList = []

def read_input ( ):
    integerLine = sys.stdin.readline()
    global n
    n = int(integerLine)
    emptyLine = sys.stdin.readline()
    for i in range (0, n):
        letterLine = sys.stdin.readline()
        letterLine = letterLine.strip()
        letterLine = str(letterLine)
        letterLine = letterLine.replace('\n',"")
        letterLine = letterLine.replace(" ","")
        wordSearchList.append(letterLine)
        i+=1
    emptyLine2 = sys.stdin.readline()
    integerLine2 = sys.stdin.readline()
    k = int(integerLine2)
    for i in range (0, k):
        wordLine = sys.stdin.readline()
        wordLine = str(wordLine)
        wordLine = wordLine.replace('\n',"")
        wordList.append(wordLine)
        i+=1
    #At this point, 2 separate lists have been made. One is the list of the lines in the word search as strings
    #and the other is a list of the words we are searching for.
        
def find_horizontal(word):
    for j in range(len(wordSearchList)):  
        if word in wordSearchList[j]:
            column = wordSearchList[j].find(word)
            print (word+": ("+ str(j+1) + ", " + str(column+1)+")")
            return True
        #Checks to see if the word is forward and horizontal in the wordsearch.
        elif word in (wordSearchList[j][::-1]):
            column = wordSearchList[j][::-1].find(word)
            print (word+": ("+ str(j+1) + ", " + str((n)-column)+")")
            return True
        #Checks to see if the word is backward and horizontal in the wordsearch.
    return False

def find_vertical(word):
    indivChar = 0
    vertWordSearchList = []
    vertWordSearchListStr = ""
    while indivChar<n:
        for c in range(len(wordSearchList)):
            vertWordSearchListStr = vertWordSearchListStr + wordSearchList[c][indivChar]
            c+=1
        vertWordSearchList.append(vertWordSearchListStr)
        indivChar+=1
        vertWordSearchListStr = ""
    #This nested loop just turned the vertical columns in the grid into strings and put them
    #all into a list called vertWordSearchList.
    for j in range(len(vertWordSearchList)):
         if word in vertWordSearchList[j]:
            row = vertWordSearchList[j].find(word)
            print (word+": ("+ str(row+1) + ", " + str(j+1) +")")
            return True
        #Checks to see if the word is vertical, reading top to bottom.
         elif word in (vertWordSearchList[j][::-1]):
            row = n - vertWordSearchList[j][::-1].find(word)
            print (word+": ("+ str(row) + ", " + str(j+1) +")")
            return True
        #Checks to see if the word is vertical, reading bottom to top.
    return False
                
def find_diagonalBDRUL(word): #bottom, down right, up left, meaning the bottom left triangle of the word search at \ angle.
    indivChar = 0
    c = 0
    diagWordSearchList = []
    diagWordSearchListStr = ""
    for h in range(len(wordSearchList)):
        while indivChar<n-h:
            diagWordSearchListStr = diagWordSearchListStr + wordSearchList[c][indivChar]
            indivChar+=1
            c+=1
        c = h+1
        indivChar = 0
        diagWordSearchList.append(diagWordSearchListStr)
        diagWordSearchListStr = ""
    #Creates a list of the diagonals below and including the middle diagonal, each term reducing in size as it moves to the edge of the word search.
    for j in range(len(diagWordSearchList)):
        if word in diagWordSearchList[j]:
            column = diagWordSearchList[j].find(word)
            row = j + column
            print (word+": ("+ str(row+1) + ", " + str(column+1) +")")
            return True
        #Checks to see if the word is diagonal, reading top left to bottom right. This works for diagonals below and including the middle diag \.
        if word in diagWordSearchList[j][::-1]:
            column = n - diagWordSearchList[j][::-1].find(word)- j - 1
            row = j + column
            print (word+": ("+ str(row+1) + ", " + str(column+1) +")")
            return True
        #Checks to see if the word is diagonal, reading bottom right to top left. This works for diagonals below and including the middle diag \.
    return False
            
def find_diagonalTDRUL(word): #top, down right, up left, meaning the top right triangle of the word search at \ angle.
    indivChar = 1
    c = 0
    diagWordSearchList = []
    diagWordSearchListStr = ""
    for h in range(len(wordSearchList)-1):
        while indivChar<n:
            diagWordSearchListStr = diagWordSearchListStr + wordSearchList[c][indivChar]
            indivChar+=1
            c+=1
        c = 0
        indivChar = h+2
        diagWordSearchList.append(diagWordSearchListStr)
        diagWordSearchListStr = ""
    #Creates a list of the diagonals above the middle diagonal, each term reducing in size as it moves to the edge of the word search.
    for j in range(len(diagWordSearchList)):
        if word in diagWordSearchList[j]:
            row = diagWordSearchList[j].find(word)
            column = row + j + 1
            print (word+": ("+ str(row+1) + ", " + str(column+1) +")")
            return True
        #Checks to see if the word is diagonal, reading top left to bottom right. This works for diagonals above the middle diag \.
        if word in diagWordSearchList[j][::-1]:
            row = len(diagWordSearchList[j][::-1])-diagWordSearchList[j][::-1].find(word)
            column = j + row
            print (word+": ("+ str(row) + ", " + str(column+1) +")")
            return True
        #Checks to see if the word is diagonal, reading bottom right to top left. This works for diagonals above the middle diag \.
    return False
            
def find_diagonalBURDL(word): #bottom, up right, down left, meaning the bottom right triangle of the word search at / angle.
    indivChar = n-1
    c = 0
    diagWordSearchList = []
    diagWordSearchListStr = ""
    for h in range(len(wordSearchList)):
        while indivChar>=h:
            diagWordSearchListStr = diagWordSearchListStr + wordSearchList[c][indivChar]
            indivChar-=1
            c+=1
        c = h+1
        indivChar = n-1
        diagWordSearchList.append(diagWordSearchListStr)
        diagWordSearchListStr = ""
    #Creates a list of the diagonals below the middle diagonal, each term reducing in size as it moves to the edge of the word search.
    for j in range(len(diagWordSearchList)):
        if word in diagWordSearchList[j]:
            column = n - diagWordSearchList[j].find(word)
            row = j + diagWordSearchList[j].find(word)+1
            print (word+": ("+ str(row) + ", " + str(column) +")")
            return True
        #Checks to see if the word is diagonal, reading top right to bottom left. This works for diagonals below and including the middle diag /.
        if word in diagWordSearchList[j][::-1]:
            column = j + diagWordSearchList[j][::-1].find(word)+1
            row = n - diagWordSearchList[j][::-1].find(word)
            print (word+": ("+ str(row) + ", " + str(column) +")")
            return True
        #Checks to see if the word is diagonal, reading bottom left to top right. This works for diagonals below and including the middle diag /.
    return False

def find_diagonalTURDL(word): #top, up right, down left, meaning the top left triangle of the word search at / angle.
    indivChar = n-2
    c = 0
    diagWordSearchList = []
    diagWordSearchListStr = ""
    for h in range(len(wordSearchList)-1):
        while indivChar>=0:
            diagWordSearchListStr = diagWordSearchListStr + wordSearchList[c][indivChar]
            indivChar-=1
            c+=1
        c = 0
        indivChar = n-h-3
        diagWordSearchList.append(diagWordSearchListStr)
        diagWordSearchListStr = ""
        #Creates a list of the diagonals above the middle diagonal, each term reducing in size as it moves to the edge of the word search.
    for j in range(len(diagWordSearchList)):
        if word in diagWordSearchList[j]:
            column = n - diagWordSearchList[j].find(word)-j-1
            row = diagWordSearchList[j].find(word)+1
            print (word+": ("+ str(row) + ", " + str(column) +")")
            return True
        #Checks to see if the word is diagonal, reading top right to bottom left. This works for diagonals above the middle diag /.
        if word in diagWordSearchList[j][::-1]:
            column = diagWordSearchList[j][::-1].find(word)+1
            row = n - diagWordSearchList[j][::-1].find(word)-j-1
            print (word+": ("+ str(row) + ", " + str(column) +")")
            return True
        #Checks to see if the word is diagonal, reading top right to bottom left. This works for diagonals above the middle diag /.
    return False
    
def find_word():
    for word in wordList:
        if find_horizontal(word):
            continue
        elif find_vertical(word):
            continue
        elif find_diagonalBDRUL(word):
            continue
        elif find_diagonalTDRUL(word):
            continue
        elif find_diagonalBURDL(word):
            continue
        elif find_diagonalTURDL(word):
            continue
        print ((word)+ str(": (0, 0)"))
        #If the word makes it through all of the functions without returning true, the word is not in the word search and returns (0, 0)
    
                
def main():
    read_input()
    find_word()

main()
