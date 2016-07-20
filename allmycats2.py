catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = raw_input()
    if name == '':
        break
    catNames.append(str(name))  # concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
