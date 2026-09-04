t = (1, 2, 3)
try:
    t[0] = 99
    print(t)
except TypeError as e:
    print('cannot change a tuple:',e )

print(t)
