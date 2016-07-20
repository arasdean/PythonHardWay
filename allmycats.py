catNames = []
while True:
    print("Enter the name of your cat" + str(len(catNames))
    name = input()
    if name == '':
        break
    catNames += [name]
print("The cat names are: ")
for name in catNames:
    print(' ' + name)
