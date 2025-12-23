a = [10, 27, 40, 4, 76,55,9, 70]

# Make a new list which items are even
# Normal Process
newlist = []
for i in a:
    if i%2 == 0:
        newlist.append(i)
print(newlist)


# Using List Comprehention
n_list = [i for i in a if i%2 ==0]