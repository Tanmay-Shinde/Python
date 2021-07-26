"""Fibonacci Series"""
i=3
a=0
b=1

n=int(input("Enter the number of terms in the series: "))

print(a)
print(b)
while i<=n:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
    
