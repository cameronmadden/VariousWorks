#  File: Boxes.py

#  Description: This program takes a list of length n of boxes and determines which boxes fit
# 	within each other. After doing so, it returns the largest number of boxes that can fit within 
# 	one of the boxes along with the number of possible set of boxes that would be possible 
# 	in that combination. 

#  Student Name: Cameron Madden

#  Student UT EID: crm5224

#  Partner Name: Taylor Chhay

#  Partner UT EID: tsc899

#  Course Name: CS 313E

#  Unique Number: 52590 and 52595

#  Date Created: 10/15/21

#  Date Last Modified: 10/17/21

import sys

boxfits = {}

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
    box_list = box_list
    # iterates through the box_list 
    for i in range(len(box_list)):
        # stores the box as fitting within itself
        if i == 0:
            boxfits[0] = 1
        else:
            allposs = []
            boxfits[i] = 1
            k = 1
            while i - k >= 0:
	    # checks if previous box fits within current box 
                if does_fit(box_list[i - k], box_list[i]):
                    allposs.append(i-k)
                    
                    k+=1
	    # if it doesn’t fit then it checks the next box below 
                else:
                    k+=1
            
            maximum = 0
	# iterates through all possible combinations 
            for x in range(len(allposs)):
                if boxfits[allposs[x]] > maximum:
                    maximum = boxfits[allposs[x]]
                
            boxfits[i] += maximum

                
    # iterates through the list of boxes that fit     
    for j in range(len(boxfits)):
        if j == 0:
            LNOB = boxfits[j]
        else:
            if boxfits[j] > LNOB:
                LNOB = boxfits[j]
    
    # creates list of which boxes have the LNOB ( Largest number of boxes )
    highlist = []
    for l in boxfits:
        if boxfits[l] == LNOB:
            highlist.append(l)
         
            
    maxnum = LNOB-1
    NOS = 0
    while maxnum > 0:
        # stores the possible boxes that fits 
        highlistbuilder = []
        # searches all possibilities 
        for z in highlist:
            maximums = 0
            # recursion to determine how many combinations of the LNOB are possible
            maximums, highs = maxes(box_list, z, maxnum)
            NOS += maximums
            highlistbuilder += highs
            
        highlist = highlistbuilder
        maxnum -= 1    

    return (LNOB, NOS)


# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def maxes (box_list, i, maxnum):
    #This function looks at the numbers that fit in box_list[i] and only returns
    #the ones whose maxnum = maxnum in the dictionary boxfits
    allposs = []
    k = 1
    while i - k >= 0:
        if does_fit(box_list[i - k], box_list[i]):
            allposs.append(i-k)
                    
            k+=1
        else:
            k+=1

    maxes = 0
    highlist = []
    #Think of all possible combinations of boxes that fit in boxes. You can make a
    #tree diagram to see what fits in what. Once you get to the bottom of the tree, count
    #all the numbers along the bottom and you will get the total number of possibilities.
    for i in allposs:
        if boxfits[i] == maxnum and maxnum == 1:
            maxes += 1
            highlist.append(i)
        elif boxfits[i] == maxnum and maxnum != 1:
            maxes += 0
            highlist.append(i)
    return (maxes, highlist)
    
    
def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  
  #print()

  # sort the box list
  box_list.sort()
  

  # print the box_list to see if it has been sorted.

  #print (box_list)
  #print()

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes, num_sets = nesting_boxes (box_list)

  # print the largest number of boxes that fit
  print (max_boxes)

  # print the number of sets of such boxes
  print (num_sets)

if __name__ == "__main__":
  main()
