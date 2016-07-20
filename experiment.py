""""tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidth = [0] * len(tableData)
    for w in range(len(tableData[0])):
        for l in range(len(tableData)):
            if len(table[l][w]) > colWidth[l]:
                colWidth[l] = len(tableData[l][w])
    print(colWidth)

    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(table[y][x].rjust(colWidth[y] + 1), end=' ')
        print()

printTable(tableData)"""

beatles = [['John', '1940'], ['Paul', '1942'],
            ['George', '1943'], ['Ringo','1940']]


def colMaker(beatles):
    first = []
    second = []
    main = []
    for w in range(4):
        first.append(beatles[w][0])
    for l in range(4):
        second.append(beatles[l][1])

    main.append(first)
    main.append(second)
    colwidth = [0] * len(main) # [0, 0]
    for i in main:
        for j in i:
            for k in range(len(main)):
                if len(j) > colwidth[k]:
                    colwidth[k] = len(j)
    print(colwidth)

    for x in range(len(main[0])):
        for y in range(len(main)):
            print(main[y][x].rjust(colwidth[1]), end=' ')
        print()
colMaker(beatles)
