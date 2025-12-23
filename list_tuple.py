a = [1,2,3, 'x']
print(a)

a[0]=3.14
print(a)
print(len(a)) 


print(list(a))

# List Append kora
a.append("banana")
print(a)

# List Insert kora
a.insert(2,5000)
print(a)

# List Extend kora
b = ['a', 'b', 'c']
print(b)
a.extend(b)
print(a)

# Reverse kora
a.reverse()
print(a)

### Tuple ###
x = (1, 2, 3)
y = tuple(reversed(x))
print(x,y)