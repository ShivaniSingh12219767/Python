f = open("Python/Files/demo2.txt","r",encoding="utf-8")
f1=open("Python/Files/demo1.txt","w")
f1.write("Hi there!!!\n My name is Shivani Singh\n  Currently I am Pursuing Btech CSE from Lovely Professional University\n")

for i in f:
    f1.write(i)
    
try:
    f=open("Python/Files/demo2.txt")
    # Your code goes here
finally:
    f.close()
f1.close()
