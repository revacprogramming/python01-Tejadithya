# Dictionaries
hand = open("mbox-short.txt")
di = dict()
for line in hand:
    words = line.split()
    if len(line)<2 or words[0] != "From":
        continue
    word = words[1]
    di[word] = di.get(word,0) + 1

largest = -1
largmail = None
for e,c in di.items():
    if c >largest:
        largest = c
        largmail = e
print(largmail,largest)