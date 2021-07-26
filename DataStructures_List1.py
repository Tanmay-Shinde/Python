"""Data Structures_List"""

l1 = ["C","C++","Python"]
print(l1)
print(l1[1])

print(len(l1))
print(len(l1[1]))

l1.append("Java")
print(l1)
l1.insert(1,"Java")
print(l1)

l1.remove("C++")
print(l1)

l2=["D","A","C","B"]
print("Old List:")
print(l2)
l2.sort()
print("New List:")
print(l2)
l2.sort(reverse=True)
print("Reverse Sort")
print(l2)
