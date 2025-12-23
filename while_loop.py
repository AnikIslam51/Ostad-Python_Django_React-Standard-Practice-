# Find the sum of all the items in the list
a = [4, 6, 89, 100, 45, 67, 67, 84, 67]
sum = 0

i=0
while i < len(a):
    sum += a[i]
    i+=1

print(sum)