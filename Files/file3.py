with open("Python/Files/demo2.txt") as f:
    print(f.read(5))
    print(f.read(11))
    print(f.read())
    print(f.tell())
f1=open("Python/Files/Shivani.jpeg","rb")
# print(f1.read())
f2=open("Python/Files/img_copy.jpeg","wb")
for i in f1:
    f2.write(i)
    
    
    
# How to  Remove files
import os
if os.path.exists("Python/Files/demo.txt"):
    os.remove("Python/Files/demo.txt")
else:
    print("File does not exists")