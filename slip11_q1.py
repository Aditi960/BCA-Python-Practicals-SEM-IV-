# Python code for Slip 11, Question 1

str=input("enter string := ")
counter=0
for char in str:
    if char != " ":
        counter+=1
print(counter)