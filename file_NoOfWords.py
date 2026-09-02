f=open("example.txt","r")
lines=f.readlines()

words=" ".join(lines).split()
print("Total number of words in file example.txt is: ",len(words))
f.close()

#OR

File1 = open("example.txt", "r")
ctr = 0
for i in File1:
        words = i.split() 
        ctr += len(words)
print ("Total number of words in file example.txt is: ", ctr)
File1.close()