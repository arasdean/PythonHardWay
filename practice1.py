beatles = [['John', '1940'], ['Paul', '1942'],
            ['George', '1943'], ['Ringo','1940']]
#colwidth = 2

def transposeThis(beatles):
    colwidth = [0] * len(beatles)
    for i in range(len(beatles)):
        for j in range(1):
            if len(beatles[i][j]) > colwidth[j]:
                colwidth[j] = len(beatles[i][j])
    print(colwidth)

    for a in range(4):
        for b in range(2):
            print(beatles[a][b].rjust(6) + beatles[a+1][b].rjust(6))
transposeThis(beatles)
