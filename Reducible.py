#  This program incorporates stdin in the command line and looks through
# a list of every word in the dictionary to find the longest 'reducible' word.
# Reducible in this case means that you can take out one letter of the word
# and still have the resulting word be in the dictionary all the way down to
# one letter. For example: [amp -> am -> a], therefore amp is reducible. Because
# there are so many words, hashing is used to speed up to process by eliminating
# possible words as it goes.

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

def step_size (s, const = 3):
    deg = len(s)-1
    key = 0
    for ch in range(len( s)):
        key += (ord(s[ch])-96)* 26**(deg)
        deg -= 1
    return const - (key % const)

def insert_word (s, hash_table):
    idx = hash_word(s, len(hash_table))
    j = 0
    while j == 0:
        if idx >= len(hash_table):
            idx = idx - len(hash_table)
        if hash_table[idx] == '':
            hash_table[idx] = s
            j = 1
        else: idx += step_size(s, 3)
    

def find_word (s, hash_table):
    idx = hash_word(s, len(hash_table))
    while hash_table[idx] != '':
        if hash_table[idx] == s:
            return True
        else:
            idx += step_size(s, 3)
            if idx >= len(hash_table):
                idx = idx - len(hash_table)
    return False

def is_reducible (s, hash_table, hash_memo):
    if len(s) == 1:
        insert_word(s, hash_memo)
        return True
    else:
        idx = 0
        while idx < len(s):
            d = (s[0: idx] + s[idx+1::])
            if find_word(d, hash_memo):
                if find_word(s, hash_memo):
                    insert_word(s, hash_memo)
                return True
            elif find_word(d, hash_table):
                if is_reducible(d, hash_table, hash_memo):
                    insert_word(d, hash_memo)
                    return True
            idx += 1
    return False

def get_longest_words (string_list):
    longwordslist = []
    k = 0
    for i in string_list:
        if len(i) > k:
            k = len(i)
    for i in string_list:
        if len(i) == k:
            longwordslist.append(i)
    return longwordslist

    
def main():
  # create an empty word_list
  word_list = []

  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  k = 2*len(word_list)+1
  while k >= 2*len(word_list):
      if is_prime(k):
          N = k
          break
      else:
          k+=2

  hash_list = []
  
  for num in range(0,N):
      hash_list.append('')

  for i in word_list:
      insert_word(i, hash_list)
  insert_word('a', hash_list)  
  insert_word('i', hash_list)
  insert_word('o', hash_list)
      
  #print (hash_table)
      
  hash_memo = []
  
  k = int(round(0.2*len(word_list))+1)
  while k >= 0.2*len(word_list):
      if is_prime(k):
          M = k
          break
      else:
          k+=2

  for i in range(M):
      hash_memo.append('')
      
 
  reducible_words = []
  #print (word_list)
  
  for word in (word_list):
      if 'a' not in word and 'o' not in word and 'i' not in word:
          continue
      elif is_reducible(word, hash_list , hash_memo):
          #print (word)
          reducible_words.append(word)

          
  # find the largest reducible words in reducible_words
  finallist = get_longest_words (reducible_words)
  finallist.sort()
  
  for i in finallist:
      print (i)

if __name__ == "__main__":
  main()
