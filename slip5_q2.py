# Python code for Slip 5, Question 2
t=(1,1,1,2,3,4,4,4)

repeat=[x for x in t if t.count(x)>2]
print(set(repeat))