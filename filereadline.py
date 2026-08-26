f=open("example.txt","r")
print(f.readline())
print(f.readline())
f.close()


f=open("example.txt","r")
print(f.readlines())
f.close()
