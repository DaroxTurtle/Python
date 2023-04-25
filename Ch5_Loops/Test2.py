smallest_so_far = None 
# Since I'm looking for smallest number on the_num[]. We would put None as we don't know what the smallest number, so we use None bc it is not a number.

print('Before', smallest_so_far) 
for the_num in [9, 41, 12, 3, 25, 60]:
    if smallest_so_far is None:
        smallest_so_far = the_num

    elif smallest_so_far > the_num:
        smallest_so_far = the_num

    print(smallest_so_far, the_num)
print('After', smallest_so_far)