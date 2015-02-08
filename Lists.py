__author__ = 'cook'

## Declaring an empty list
L = []
print(len(L))
L1 = list()
## Indexing lists
L2 = ['a', 'b', 'c']
print(L2[1])

## Adding elements to a list
print('\nAdding\n')
L.append(1)
L.append(2)
print(L)
print(max(L))
L2[2] = 'd'
print(L2)
## Removing elements from a list
print('\nRemoving\n')
L.remove(1)
print(L)
print(L2)
del(L2[1])
print(L2)
## List methods
### String Splitting
print('\nSplitting\n')
L3 = 'sassaddffga'.split('sa')
print(len(L3))
print(L3)