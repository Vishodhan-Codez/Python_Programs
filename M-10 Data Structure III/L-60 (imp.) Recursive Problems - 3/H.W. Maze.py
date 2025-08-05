combo = []
def posout(maze, combo, row, col, rows, cols): #maze - grid , combo - output , row - current row , col - current column
    if row == rows - 1 and col == cols - 1:
        print(''.join(combo))
        return
    if col + 1 != cols:
        combo.append('r')
        posout(maze, combo, row, col + 1, rows, cols)
        combo.pop()
    if row + 1 != rows:
        combo.append('d')
        posout(maze, combo, row + 1, col, rows, cols)
        combo.pop()

cols = int(input("Enter the number of columns: "))
rows = int(input("Enter the number of rows: "))
maze = []
count = 1
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(count)
        count += 1
    maze.append(row)
posout(maze, combo, 0, 0, rows, cols)
# R | 2 | 3
# 4 | 5 | 6
# 7 | 8 | T