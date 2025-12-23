a = [1,2,3,4,5, 'a', 6,7,8,9,10]
print(a)

# break statement
for i in a:
    if type(i) == type('str'):
        break
    else:
        print(i)


# continue statement
for i in a:
    if type(i) == type('str'):
        continue
    else:
        print(i)