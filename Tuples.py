__author__ = 'cook'

## Create an empty tuple
T1 = ()
T2 = tuple()

## Tuple indexing
T3 = ('1', '2', '3')
print(T3)
print(T3[-1])

## Adding elements to a tuple
T3 = T3 + ('4',)
print(T3)
L3 = list(T3)
print(L3)
L3.append('5')
print(L3)
T3 = tuple(L3)
print(T3)

## Removing elements from a tuple
print("That's not a good idea.")

## Tuple methods
print("Yeah, we don't have those.")