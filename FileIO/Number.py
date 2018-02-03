filename = "number.txt"
numberfile = open("number.txt","r+");

numberline = 0
numberwords = 0
numberchar = 0

for line in numberfile:
    words=line.split();
    numberline = numberline + 1;
    numberwords = len(words);
    numberchar = len(line);
    



print (numberlines.read());
