print('E8.3_042823.py')

# Exercise 8.3
# Rewrite the guardian code in the above example without the two if statements.
# Instead, use a compound logical expression using the ore logical operator with a single if statement.

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()

    # Guardian Pattern in a compound statement
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])