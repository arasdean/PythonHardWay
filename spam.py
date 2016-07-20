grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#I need to use a loop
#one loop will access one element of the list
# one loop will access the list within that single element
#This second loop will print out the first item of the list in the first element
# then the count will increase, thus moving to the second element of Grid
#then the second loop does what it does to the second elements of each list
#Each does this until there is no more to be printed
#meaning the loops are restricted by length
# Each element of Grid has 6 parts, and there are 9 elements
for j in range(len(grid[0])):
    for i in range(0, len(grid)):
        print grid[i][j],
    
    print()

#Why does range do in a for loop?
    # why is range necessary in this scenario?
#Why j before i? Does this make a difference?
#Why is are we printing 'grid[i][0]' vs [i][j]?
# Why are we deleting grid[i][0]



# as of now, the problem is that the while/for loops
# do not continue on the next set of ekenebts ]
