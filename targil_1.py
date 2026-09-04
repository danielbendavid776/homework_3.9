prices = {'apple': 12, 'banana': 7, 'cherry': 25}
print(prices)
try:
    key = input("Which fruit? ")
    print(prices[key])
except KeyError:
    print(f'{key} not exist')

print('goodbye')