numberlist=[];


Number=int (input("Enter a number"))


for i in range(1,Number+1):
    if (Number%i ==0):
        numberlist.append(i)
print (numberlist);
