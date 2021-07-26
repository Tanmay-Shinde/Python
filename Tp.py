import operator
str = input("Please enter a string: ")
str = str.lower()
l = len(str)
Dict = {}
a=0

def most_frequent(st):
    i = 0
    while i < l:
        k=1
        a=0
        ch = st[i]
        if i == 0:
            j = 1
            while j<l:
                ch2 = st[j]
                if ch == ch2:
                    k+=1
                j+=1
                
            Dict[ch] = k
        
        else:
            b = i-1
            while b >= 0:
                ch3 = st[b]
                if ch == ch3:
                    a = 1
                    break
                b-=1

            if a == 0:
                m = i+1
                while m<l:
                    ch4 = st[m]
                    if ch == ch4:
                        k+=1
                    m+=1    
                Dict[ch] = k             
        i+=1
        
    sorted_d = dict( sorted(Dict.items(), key=operator.itemgetter(1),reverse=True))
    
    for x,y in sorted_d.items():
        print(x,"=",y)

most_frequent(str)
