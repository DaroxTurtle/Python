print('N7.1_042423.py')

# --- --- --- File Processing --- --- ---
# Text files are a sequence of lines,
# Such as hello.py.

# --- --- --- Opening a File --- --- ---
# To read a file we use the open() function
# open() returns a 'file handle'

# -- -- Using open() -- --
# handle = open(filename, mode)
# fhand = open('mbox.txt', r)

# fhand is a pneumonic with the purpose of returning a handle of the manipulated file
# 'mbox.txt' is a string
# r which is mode is optional and should be 'r' if we are planning to read the file, while
# 'w' if we are going to write to the file.

# --- --- --- What is a handle? --- --- ---
# Handle is the connector to the file,
# it allows you to do actions to the file you are accessing.
# -- -- -- What if Files are Missing? -- -- --
# If file is missing it becomes a traceback.

# --- --- --- The newline Character --- --- ---
# newline indicades that the line ended.
# We represent newline as \n in strings.
# stuff = 'hello\nWorld!'
# the \n on stuff is a new line.
# This counts another character on len() function.
