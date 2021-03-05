def countWordsFromFile():
    fileName=input("Enter the File Name ")
    NoOfWords=0
    lines=1
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        NoOfWords=NoOfWords+len(words)
    
    for i in file:
    
        if (i=='/n'):
            lines=lines+1   
    print("No Of Words ")
    print(NoOfWords)
    print("Number of lines = ")
    print(lines)


countWordsFromFile()
    