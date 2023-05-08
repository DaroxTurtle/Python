print('N12.4_050723.py')

# I feel like the way I'm learning to code this is too old fashion...
# But I could be wrong.
# However, there was an issue with 12.3 I couldn't make the code run, :>

# --- --- --- Characters, ASCII, and Unicode --- --- ---
# ASCII     - American Standard Code for Information Interchange

# -- -- -- Representing Simple Strings -- -- --
# Each character is represented by a number between 0 and 256 stored in 8 bits of memory
#
# We refer to 8 bits of memory as "byte" of memory.
#
# The ord() function tells us the numeric value of a simple ASCII character.

# -- -- -- Multi-Byte Characters -- -- --
# To represent the wide range of characters computers must handle we represent
# characters with more than one byte
    # UTF-16    - Fixed Length      - Two bytes
    # UTF-32    - Fixed Length      - Four Bytes
    # UTF-8     1-4 bytes
        # Upwards compatible with ASCII
        # Automatic detection between ASCII and UTF-8
        # UTF-8 is recommended practice for encoding data to be exchanged between systems

# -- -- -- Python3 and Unicode -- -- --
# Python3, all strings internally are UNICODE.
#
# Working with string variables in Python programs and reading data from files usually 'just works'
# When working with network resources the data will most likely be UTF-8.

# -- -- -- Python Strings to Bytes -- -- --
# When we talk to an external resource like a network sockets we send bytes,
# so we need to encode Python3 strings into a given character encoding.

# When we read data from an external resource, we must decode it based on
# the character set so it is properly represented in Python 3 as a string.
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# Continue to Making HTTP Easier with urllib.

