words=input("Enter Your Name : ")
print(words)
intro=input("Enter Introduction : ")
print(intro)
characterCount=0
wordCount=1

for i in intro:
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1
    
print("Number of Characters = ")
print(characterCount)
print("Number of Words = ")
print(wordCount)

