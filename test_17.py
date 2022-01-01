# sort()
# sorted()

# arr=[5,4,8,3] #list
# print(sorted(arr))


arr = ['banana', 'apple', 'pineapple', 'pear', 'peach']
# print(sorted(arr, key=len))

# print(*sorted(arr,key = lambda x:x[2]))

print(*sorted(arr, key=lambda x: x[2] or len))
# print(*sorted(arr,key=lambda x:(x[2],len(x))))