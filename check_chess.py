"""Given a chessboard with one King (K) and one Queen (Q), define a function
that tkes the coordinates for each piece and returns True if K in check.

The coordiantes are given as (column, row) where column in A-H, row in 1-8.
"""

coord_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
coord_map_rev = {v: k for k, v in coord_map.iteritems()}

def check(k_coor, q_coor):
    """Given coordinates of K and Q, return True if K in check.
    >>> check("D6", "H6")
    True

    >>> check("E6", "E4")
    True

    >>> check("B7", "D5")
    True

    >>> check("A1", "H8")
    True

    >>> check("A8", "H1")
    True

    >>> check("D6", "H7")
    False

    >>> check("E6", "F4")
    False
    """
    # convert alpha_num coordinates to num_num coordinates
    # import pdb; pdb.set_trace()
    k_coord = an_to_nn(k_coor)
    q_coord = an_to_nn(q_coor)
    qx = q_coord[0]
    qy = q_coord[1]

    # FIND ALL POSSIBLE MOVES FOR QUEEN
    q_moves = []

    # vertical
    vert = [[qx, y] for y in range(0, 8)]
    q_moves.extend(vert)
    
    # horizontal
    horiz = [[x, qy] for x in range(0, 8)]
    q_moves.extend(horiz)
    
    # diagonals
    # primary diagonal
    diag_coord(q_coord, q_moves, 1, -1)
    diag_coord(q_coord, q_moves, -1, 1)
    # secondary diagonal
    diag_coord(q_coord, q_moves, 1, 1)
    diag_coord(q_coord, q_moves, -1, -1)

    print "-"*40
    print "QUEEN MOVES"
    for pair in q_moves:
        print pair

    print '-'*40
    print "PRINTING BOARD"
    print_board(k_coord, q_coord, q_moves)

    # check if k_coord in q_moves
    if k_coord in q_moves:
        return True

    return False


# Helper functions
def an_to_nn(alpha_num_coord):
    """Convert A-H/1-8 coordinate to 0-7/0-7 coordinate.
    
    >>> k_coor = 'D6'
    >>> an_to_nn(k_coor)
    [3, 5]
    """

    # split coordinate
    x = alpha_num_coord[0]
    y = int(alpha_num_coord[1]) - 1
    # convert letter to number
    x = coord_map[x]
    # return list
    return [x,y]

def nn_to_an(num_num_coord):
    """Convert 0-7/0-7 coordinate to A-H/1-8 coordinate
    
    >>> nn_to_an([0,0])
    'A1'
    >>> nn_to_an([7,7])
    'H8'
    """
    x = num_num_coord[0]
    y = str(num_num_coord[1] + 1)
    # convert x number to letter
    x = coord_map_rev[x]
    # return a string xy
    return x + y

def diag_coord(start, lst, dir1, dir2):
    """Append diagonal coordinates to list.

    Given a starting coordinate, a list of coordinates, and quadrant directions,
    append the coordinates to the list.

    start: starting coordinate, e.g. (2, 4)
    lst: coordinates for Queen moves
    dir1: +/- 1 (x direction)
    dir2: +/- 1 (y direction)
    """
    # import pdb; pdb.set_trace()
    x = start[0] + dir1
    y = start[1] + dir2

    while x in range(0, 8) and y in range(0, 8):
        lst.append([x,y])
        x += dir1
        y += dir2
    return

def print_board(k_coor, q_coor, q_moves):
    """Print the pieces and moves"""
    
    board = []
    for y in range (0,8):
        curr_row = ''
        for x in range(0,8):
            if [x, y] == q_coor:
                curr_row += 'Q'
            elif [x, y] == k_coor:
                curr_row += 'K'
            elif [x, y] in q_moves:
                curr_row += '*'
            else:
                curr_row += '-'
        board.append(curr_row)
    # import pdb; pdb.set_trace()
    for row in board:
        print row

if __name__ == '__main__':
    king = 'D6'
    queen = 'H6'
    check(king, queen)
