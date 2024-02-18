import os
from collections import Counter
import socket

def countWords(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        return len(words)

def topWords(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        wordCounts = Counter(words)
        return wordCounts.most_common(3)

files = os.listdir('/home/data')
print("Files in /home/data directory:")
for file in files:
    print(file)

totalWords = 0
for file in files:
    if file.endswith('.txt'):
        filePath = os.path.join('/home/data', file)
        wordsCount = countWords(filePath)
        print(f"Total words in {file}: {wordsCount}")
        totalWords += wordsCount

topWordsList = topWords('/home/data/IF.txt')
print("Top 3 words with maximum counts in IF.txt:")
for word, count in topWordsList:
    print(f"{word}: {count}")

hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)
print(f"IP Address of the machine: {ipAddress}")

with open('/home/output/result.txt', 'w') as resultFile:
    resultFile.write("Files in /home/data directory:\n")
    for file in files:
        resultFile.write(file + '\n')

    resultFile.write("\n")
    for file in files:
        if file.endswith('.txt'):
            filePath = os.path.join('/home/data', file)
            wordsCount = countWords(filePath)
            resultFile.write(f"Total words in {file}: {wordsCount}\n")

    resultFile.write("\nTop 3 words with maximum counts in IF.txt:\n")
    for word, count in topWordsList:
        resultFile.write(f"{word}: {count}\n")

    resultFile.write(f"\nIP Address of the machine: {ipAddress}\n")

with open('/home/output/result.txt', 'r') as resultFile:
    print("\nContents of result.txt:")
    print(resultFile.read())
