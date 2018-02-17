

filename = "constitution.txt"
numberfile = open("constitution.txt","r+");

numberwords=0
numberchar=0

for line in numberfile:
    words=line.split();
    numberwords = numberwords+ len(words);
    for word in words:
        numberchar= numberchar + word.count ("p")

print (numberchar);




