# Python code for Slip 3, Question 1
tuple=(1,2,3,4,4)

repeat=[x for x in tuple if tuple.count(x)>1]

print(set(repeat))