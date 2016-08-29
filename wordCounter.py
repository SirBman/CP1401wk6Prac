

strInput = str(input("Please enter a lot of words."))

strInput.strip()
strInput.lower()
wordList = strInput.split()

wordCount = {}

for word in wordList:
    if word in wordCount:
        wordCount[word] +=1
    else:
        wordCount[word] = 1


for word, count in wordCount.items():
    print("{}: {}".format(word, count))
