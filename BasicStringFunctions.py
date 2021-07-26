"""Basic String Functions"""

str_1 = "MyCaptain"
print(str_1)

print(str_1[1]) #y  same as str_1.charAt(1)

print(str_1[2:5]) # same as
print(str_1[2:])
print(str_1[-1:])
print(str_1[-9])
print(str_1[-2:])

print("MyCaptain"[::])
print(str_1[0:9:2]) #[start, end, step]

print(str_1.replace("a","z",1))
print(str_1.replace("a","z",2))
print(str_1[0:6] + "z" + str_1[7:])

a = "hello"
print(a.upper())

b= "HELLO"
print(b.lower())

print(a.split("l"))
