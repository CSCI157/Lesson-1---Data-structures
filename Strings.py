__author__ = 'cook'

## What are strings?
print('What are strings?')
s1 = 'Hello World'
s2 = 'Adios Amigos'
print(s1)
print(s2)
print(len(s1))

## String indexing.
print('\nString Indexing')
s3 = s1[0]
s4 = s1[2:4]
s5 = s1[2:]
print(s3)
print(s4)
print(s5)
print(s1[:8])
print(s1[-3:-1])
print(s1[-3:])

## String methods
print('\nString Methods:')
### Concatenation
print('\n Concatenation')
s6 = s1 + ' ' +  s2
print(' '*3 + s6)
print('   ' + s1 + '  ' + s2[1:4])
### Capitalization
print('\n Capitalization')
print('   ' + s2.upper())
print('   ' + s2.lower())
print('   ' + s2.title())
### Stripping
print('\n Stripping')
print('   ' + 'aaddaassa'.strip('a'))
print('   ' + 'aaddaassa'.rstrip('a'))
print('   ' + 'aaddaassa'.lstrip('a'))
### In and find
print('\n In and find')
if 'a' in 'aaddaassa':
    print('   ' + 'aaddaassa contains an a')
else:
    print('   ' + 'aaddaassa does not contain an a')
print('   ' + str('aaddaassa'.find('a')))

