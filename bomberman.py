#Hackerrank Bomberman on Hackerrank
#Needs optimisation (time out)


def replace_char (str, chr, length, pos):
    str2 = str[:pos]+chr+str[pos+1:]
    return str2
    
def bomb (str, mat, r, c):        
    for i in range(r):
        for j in range (c):
            if (str == "put bombs" and mat[i][j]=='.'):
                mat[i]=replace_char(mat[i],'*', c, j)
                #mat[i][j]='*'
            if (str == "explode" and mat[i][j]=='O'):
                mat[i] = replace_char(mat[i], '.', c, j)
                adjacent_positions = [
                (i-1, j), (i+1, j), (i, j+1), (i, j-1)]
                for x, y in adjacent_positions:
                    if ((0<= x < r) and (0 <= y < c) and (mat[x][y]!= 'O')):
                        mat[x]=replace_char(mat[x], '.', c, y)
                        #mat[x][y]= '.'
            if (str == "reset" and mat[i][j]=='*'):
                mat[i]=replace_char(mat[i], 'O', c, j)
                #mat[i][j] = 'O'
    return (mat)



def parce (grid, r, c, n):

    for i in range (0, n-1):
        if (i%2 == 0):
            grid = bomb("put bombs", grid, r, c)
        if (i%2 == 1):
            grid = bomb ("explode", grid, r, c)
            grid = bomb ("reset", grid, r, c)
        #print ('\n', i+2)
        #print('\n'.join(grid))

    grid = bomb ("reset", grid, r, c)  
    return (grid)

def find_loop (grid_storage, grid):
    if grid in grid_storage:
        return 1
    grid_storage.append(grid)
    return 0
    
def bomberMan(n, grid):
    r = len(grid)
    c = len(grid[0])
    if (n==0 or n==1):
        return (grid)
    else:
        return parce(grid, r, c, n)
    


if __name__ == '__main__':
    n = 23
    grid = ['.......O',
            '..O.O...',
            '.O...O..',
            '........',
            'O.O...O.',
            'OO......']
    
    print ('\n'.join(bomberMan (n, grid)))
