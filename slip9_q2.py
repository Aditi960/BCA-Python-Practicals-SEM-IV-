# Python code for Slip 9, Question 2
str=input("enter a string\n")
dictt={}
for char in str:
    if char in dictt:
        dictt[char]+=1
    else:
        dictt[char]=1

print("Character frequence is :- ",dictt)
