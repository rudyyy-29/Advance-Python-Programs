f= open("example.txt","r")
f= open("example2.txt","w")
f.write("This is the first line.\n")
l=["\nHello", "Welcome" ,"to", "Python", "Programming"]
f.writelines(l)
print("Number of characters written in file:",l)
f.close()
