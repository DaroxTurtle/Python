print('ex_09.py')

fname = input('Enter file: ')
fhand = open(fname)
wd = dict()

for line in fhand:
    line = line.rstrip().split()
    for word in line:
        # idiom: retrieve/ create/ update counter
        wd[word] = wd.get(word, 0) + 1
        # print(word, 'new', wd[word])
#print(wd)

# now we want to find the most common word
largest = -1
theword = None
for k,v in wd.items():
    if v > largest:
        theword = k
        largest = v

print(theword, largest)