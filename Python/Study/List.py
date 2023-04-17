#List are used to store multiple items in a single variable.

#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple,Set, and Dictionary, all with different qualities and usage.
a = ['Sigma', 'Horizon', 7, 9]
print(a)

#List +
b = [' Destiny ', 666]
c = [' Look ', 875]
print(b + c)

#List *
d = b * 3
print(d) 
e = b * 0
print(e)

#list lenth = 8
g = [3, 6, 9, 12, ' Sky ', ' Ground ', 7, 27]
print(g)
#Index
print(g[0])
print(g[1])
print(g[3])
print(g[7])

#Reverse index
print(g[-1])
print(g[-3])

#List value retouch
print(g)
g[0] = 1
print(g)
g[3] = ' Titan '
print(g)
g[-3] = ' Sea '
print(g)

#List slicing
print(g[0:4])
print(g[1:])
print(g[:5])

#List half
z = int(len(g) / 2)
print(g[:z])
print(g[-2:])
print(g[-5:-1])
print(g[:-6])
print(g[:])