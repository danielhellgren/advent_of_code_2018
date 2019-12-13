class Cart:
    #cart directions have to be in order
    # UP RIGHT DOWN LEFT as de/incrementing is used for turning
    CART_DIR_UP = 0
    CART_DIR_DOWN = 2
    CART_DIR_LEFT = 3
    CART_DIR_RIGHT = 1

    ROT_LEFT = -1
    ROT_RIGHT = 1

    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction
        self.intersection_mode = 0
        print("Added a cart at pos: " + str(pos[0]) + ", " + str(pos[1]))
    
    #Rotate cart based on dir
    # for instance UP - rotate right -> Right
    def rotate(self, rot_dir):
        new_dir = (self.direction + rot_dir) % 4
        self.direction = new_dir
        
    #turns cart if it should
    #ie on an intersection or turn
    def turn(self, cur_pos_type):
      
        #on an intersection
        #intersection turning rules
        if(cur_pos_type == "+"):

            if(self.intersection_mode == 0):
                self.rotate(Cart.ROT_LEFT)
            if(self.intersection_mode == 2):
                self.rotate(Cart.ROT_RIGHT)

            self.intersection_mode = (self.intersection_mode + 1) % 3
        
        elif(cur_pos_type == "/"):
            #if coming from above or below the cart will turn right
            #ternary operator
            self.rotate(Cart.ROT_RIGHT) if (self.direction == Cart.CART_DIR_UP or self.direction == Cart.CART_DIR_DOWN) else self.rotate(Cart.ROT_LEFT)
            
            #if self.direction == Cart.CART_DIR_UP or self.direction == Cart.CART_DIR_DOWN:
            #    self.rotate(Cart.ROT_RIGHT)
            #else:
            #    self.rotate(Cart.ROT_LEFT)

        elif(cur_pos_type == "\\"):
            #if coming from above or below the cart will turn left
            self.rotate(Cart.ROT_LEFT) if (self.direction == Cart.CART_DIR_UP or self.direction == Cart.CART_DIR_DOWN) else self.rotate(Cart.ROT_RIGHT)

            #if self.direction == Cart.CART_DIR_UP or self.direction == Cart.CART_DIR_DOWN:
            #    self.rotate(Cart.ROT_LEFT)
            #else:
            #    self.rotate(Cart.ROT_RIGHT)


    #changes carts position based on cart direction
    def move(self, track_matrix):

        pos_x = self.pos[0]
        pos_y = self.pos[1]
        
        if self.direction == Cart.CART_DIR_UP:
            pos_y -= 1
        elif self.direction == Cart.CART_DIR_DOWN:
            pos_y += 1
        elif self.direction == Cart.CART_DIR_LEFT:
            pos_x -= 1
        elif self.direction == Cart.CART_DIR_RIGHT:
            pos_x += 1

        self.pos = (pos_x, pos_y)

        self.turn(track_matrix[pos_y][pos_x])
        
    def printCart(self):
        print(" ("+ str(self.pos[0]) + ", " + str(self.pos[1]) + ") ")

    def getPosY(self):
        return self.pos[1]

    def getPosX(self):
        return self.pos[0]

    def getIntersectionMode(self):
        return self.intersection_mode

    def getDirection(self):
        return self.direction

    def getPos(self):
        return self.pos