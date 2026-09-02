File1=open("example.txt","r")
print("Current file pointer position:",File1.tell())
print(File1.read())
print("current file pointer position:",File1.tell())

File1.seek(15)

print("Current file pointer position after seek:",File1.tell())
print.read()