thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)