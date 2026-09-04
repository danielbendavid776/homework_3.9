fruits = ["apple", "banana"]
try:
    fruits.remove("orange")
    print(fruits)
except ValueError as e:
    print('orange is not in the list:', e)

print(fruits)
print('goodbye')

'''
fruits = ["apple", "banana"]
if "orange" in fruits:
    fruits.remove("orange")

print(fruits)
print('goodbye')
'''