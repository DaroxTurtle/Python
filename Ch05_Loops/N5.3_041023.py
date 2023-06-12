print('N5.3_041023.py')

# --- --- --- Loop Idioms --- --- ---

largest_so_far = -1
print('Before', largest_so_far)
for thing in [9, 41 , 12, 3, 74, 15] :
    if thing > largest_so_far :
        largest_so_far = thing
print('After', largest_so_far)

# Since we started with -1
# Whatever is inside the bracket found in the "for thing in []"
# It will replace -1 with a larger number.
# Basically finding which number is bigger by comparing it by the previous number held, with the next number in the brackets.
