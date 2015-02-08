__author__ = 'cook'

## Declaring an empty dictionary
D1 = {}
D2 = dict()

## Indexing  a dictionary - key:value
D1 = {1: 's', 2: 'hello'}
print(D1)
print(D1[1])
print(D2)

## Adding elements to a dictionary
D1[3] = 'world'
D2.update({"oh my": "Mr. Sulu"})
print(D1)
print(D2)
print(D2["oh my"])
D3 =  dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(D3)

## Removing elements from a dictionary
del(D1[2])
print(D1)

## Dictionary methods
print('sape' in D3)
