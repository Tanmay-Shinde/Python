import math
r = float(input("Input the radius of the circle: "))
ar = math.pi*r*r
print("The area of circle is: ")
print(ar)


s = input("Input the Filename: ")
print("The extension of the file is: ")
l = len(s)

i = 0
while i<l:
    ch = s[i]
    if ch == '.':
        st = s[i+1:]
        break
    i+=1

if(st == "py"):
    print("python file")
elif(st == "mp3"):
     print("MP3 Audio file")
elif(st == "zip"):
     print("Zip compressed file")
elif(st == "sql"):
     print("SQL Database file")
elif(st == "jar"):
     print("Java archive file")
elif(st == "apk"):
     print("Android package file")
elif(st == "docx"):
     print("Word document")
elif(st == "jpg"):
     print("JPEG Image file")
elif(st == "html"):
     print("HTML file")
else:
    print("Does not exist")
     
    
