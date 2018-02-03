
filename = "constitution.txt"
numberfile = open("constitution.txt","r+");

numberwords = 0

for line in numberfile:
    words=line.split();
    numberwords = numberwords+ len(words);
    
print (numberwords);




