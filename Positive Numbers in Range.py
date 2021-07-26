"""Positive Numbers"""

# creating an empty list 
List1 = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    List1.append(ele) # adding the element 

print("List1 = ", end =" ")
print(List1) 

i=0
while i < n:
    x = List1[i]
    if x > 0:
        print(x, end = ", ")
    i+=1
