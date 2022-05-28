# Files
fname = input("Enter file name: ")
fh = open(fname)
count = 0
sun = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        ipos = line.find(":")
        piece = line[ipos+1:]
        value = float(piece)
        count = count + 1
        sun = sun + value
print('Average spam confidence:', sun/count)