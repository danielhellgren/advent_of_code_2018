from cart import Cart

def getInputs(filename = "input.txt"):

    #open file
    puzzle_input_file = open(filename, "r")
    inputs = []

    #load each line into array
    for line in puzzle_input_file.readlines():

        inputs.append(str(line))

    #close file, not neccesary when read only
    puzzle_input_file.close()
    return inputs

#converts a line into an array
#adds a cart to list if there is on this line
def loadLine(line, y, carts):

    track_line = []
    x = 0

    for char in line:
        if(char == "v"):

            new_cart = Cart((x, y), Cart.CART_DIR_DOWN)
            carts.append(new_cart)

        elif(char == "^"):

            new_cart = Cart((x, y), Cart.CART_DIR_UP)
            carts.append(new_cart)

        elif(char == "<"):

            new_cart = Cart((x, y), Cart.CART_DIR_LEFT)
            carts.append(new_cart)

        elif(char == ">"):

            new_cart = Cart((x, y), Cart.CART_DIR_RIGHT)
            carts.append(new_cart)
        
        track_line.append(char)
        x += 1

    return track_line

#loads the tracks into a 2d array
#also loads carts into a list
def loadTrackMatrix(input_lines, carts):

    track_matrix = []
    y = 0

    for line in input_lines:

        track_matrix.append(loadLine(line, y, carts))
        y += 1

    return track_matrix
    

def init(filename = "input.txt"):

    raw_lines = getInputs(filename)
    carts = []
    track_matrix = loadTrackMatrix(raw_lines, carts)
    print("Loaded: " + str(len(carts)) + " carts")
    
    return track_matrix, carts

#check if any two carts are on the same location = crash
def checkCollision(carts):

    for i in range(len(carts)):
        cur_pos = carts[i].getPos()

        for j in range(i+1, len(carts)):
            if cur_pos == carts[j].getPos():

                return True, cur_pos

    return False, (0, 0)

def moveCarts(track_matrix, carts, col_detection = False):
    col_pos = (0,0)
    collision = False
    for cart in carts:
        cart.move(track_matrix)
        if col_detection:
            collision, col_pos = checkCollision(carts)
        if col_detection and collision:
            return True, col_pos
    
    return False, (0,0)

def sortCarts(carts):

    #bubble sort slow but the one i can remember atm
    n = len(carts)
    for i in range(n):

        for j in range(n-i-1):

            #if cur pos > next pos swap places
            if (carts[j]).getPosY() > (carts[j+1]).getPosY():
                carts[j], carts[j+1] = carts[j+1], carts[j]
            if ((carts[j]).getPosY() == (carts[j+1]).getPosY()) and (carts[j]).getPosX() > (carts[j+1]).getPosX():
                    carts[j], carts[j+1] = carts[j+1], carts[j]


def getCollisionPosition(tracks, carts):
    cart_collision = False
    col_pos = (0,0)
    
    while(not cart_collision):
        sortCarts(carts)
        cart_collision, col_pos = moveCarts(tracks, carts, True)

    return cart_collision, col_pos

if __name__ == '__main__':

    track_matrix, carts = init()
    sortCarts(carts)
    cart_collision, col_pos = getCollisionPosition(track_matrix, carts)

    print("Crash at: (" + str(col_pos[0]) + ", " + str(col_pos[1]) + ")")