# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:55:38 2020

@author: Fatema Akter
"""

f= open("data.txt", 'w')
f.write("if this happen, then that happens that is not good.")
f.close()

#part2-reading data
f = open("data.txt", 'r')
text=f.read()
print("this is what read from text file:  ", text)
f.close()

#part3
wordList = text.split()
print(wordList)

#part4
wordList.sort()
print(wordList)

#part 5 removing redundant words in the list

#function to get unique items
def unique(list1):
    uniqueWordList = []
    
    #traverse for all word in the wordList
    for item in list1:
        if item not in uniqueWordList:
            uniqueWordList.append(item)
    print(uniqueWordList)
unique(wordList)
