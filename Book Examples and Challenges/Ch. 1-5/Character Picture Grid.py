# grid[x][y] coordinates
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

# takes a list of list and prints on the element in hte 0 position in each list 
# then makes a new line and continues until the whole list of lists is printed

def draw_picture(list):
    for y in range(len(list[0])):
        for x in range(len(list)):
            print(list[x][y], end='')
        print('')
        
draw_picture(grid)