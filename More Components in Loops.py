"""Loop Components"""

#break
i=10
while i>0:
    print(i)
    if i==7:
        break
    i-=1

print("Loop Terminated")


#continue
i=10
while i>0:
    print(i)
    i-=1
    if i==7:
        continue

print("Loop Terminated")


#Nested Loops
i=2

while i>0:
    i=i-1
    j=5
    while j>0:
        print(j)
        j-=1
