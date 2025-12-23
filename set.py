# unorded
# unchangable
# doen't allow duplicate value
a = [1,2,2,2,3,4,4,4,5,5]
print(a)

b= set(a)
print(b)

# Union & Intersection
x = {1,2,3,4}
y = {2,3,4,5}
z = x.intersection(y)
print(z)

p = x.union(y)
print(p)