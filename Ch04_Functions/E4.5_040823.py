print('E4.5_040823.py')

# Exercise 5: What will the following Python program print out?
def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()
# a) Zap ABC jane fred jane
# b) Zap ABC Zap
# c) ABC Zap jane
# d) ABC Zap ABC
# e) Zap Zap Zap

#Answer
# ABC Zap ABC, Since jane prints "ABC" and fred "Zap", the question is asking what does it print out?
# with the sequence of jane, fred, jane. Knowing the definitions purposes.
# It will print out ABC, ZAP, ABC.

