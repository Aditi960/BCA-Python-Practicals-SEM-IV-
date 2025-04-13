# Python code for Slip 2, Question 2
from collections import Counter
dict1={'a':1,'b':3}
dict2={'b':2,'c':9}

add=Counter(dict1)+Counter(dict2)
print(dict(add))