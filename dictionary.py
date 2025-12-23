a = { 'Omuk': 14, 'Tomuk': 16, 5: [1,2,3,4,5], 10:{2,4,6,8,10}}
print(a)
print(type(a))

for i in a:
    print(i)

print("--------")
print("--------")

for i in a.values():
    print(i)

print("--------")
print("--------")

print(a.keys(), a.values())

print("--------")
print("--------")

# Using items() function
for k,v in a.items():
    print(f"Keys: {k}, values: {v}")

# Use of zip() function
a = [1,2,3]
b = ["banana","mango", "apple"]
print(zip(a,b))
print(list(zip(a,b)))
print(dict(zip(a,b)))