import unittest
#import ../solution

#importing from parent dir in python........
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import solution

from cart import Cart

class SolutionTest(unittest.TestCase):

    def init(self):
        return solution.init()

    def tick(self, tracks, carts, steps):
        for _ in range(steps):
            solution.moveCarts(tracks, carts)


    def test_loader(self):

        tracks, carts = self.init()
        #CHECK INIT
        #amount of rows
        self.assertEqual(len(tracks), 150)
        #col
        self.assertEqual(len(tracks[0]), 151)
        #amount of carts loaded
        self.assertEqual(len(carts), 17)

    def test_movement(self):

        tracks, carts = self.init()

        #intial positions
        self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_RIGHT)
        self.assertEqual(carts[0].getPos(), (60, 4))

        self.assertEqual(carts[9].getDirection(), Cart.CART_DIR_UP)
        self.assertEqual(carts[9].getPos(), (106, 74))

        self.assertEqual(carts[10].getDirection(), Cart.CART_DIR_LEFT)
        self.assertEqual(carts[10].getPos(), (35, 95))

        self.assertEqual(carts[16].getDirection(), Cart.CART_DIR_DOWN)
        self.assertEqual(carts[16].getPos(), (143, 129))

        #move one tick
        self.tick(tracks, carts, 1)
        self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_UP)
        self.assertEqual(carts[0].getPos(), (61, 4))

        self.assertEqual(carts[10].getDirection(), Cart.CART_DIR_LEFT)
        self.assertEqual(carts[10].getPos(), (34, 95))
        
        self.assertEqual(carts[9].getDirection(), Cart.CART_DIR_LEFT)
        self.assertEqual(carts[9].getPos(), (106, 73))

        self.assertEqual(carts[16].getDirection(), Cart.CART_DIR_DOWN)
        self.assertEqual(carts[16].getPos(), (143, 130))

        #total ticks 2
        self.tick(tracks, carts, 1)
        self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_UP)
        self.assertEqual(carts[0].getPos(), (61, 3))
        
       
        self.assertEqual(carts[9].getDirection(), Cart.CART_DIR_LEFT)
        self.assertEqual(carts[9].getPos(), (105, 73))

        self.assertEqual(carts[11].getDirection(), Cart.CART_DIR_DOWN)
        self.assertEqual(carts[10].getPos(), (33, 95))

        self.assertEqual(carts[16].getDirection(), Cart.CART_DIR_DOWN)
        self.assertEqual(carts[16].getPos(), (143, 131))

        #total ticks 3
        self.tick(tracks, carts, 1)
        self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_LEFT)
        self.assertEqual(carts[0].getPos(), (61, 2))
       
        self.assertEqual(carts[9].getDirection(), Cart.CART_DIR_LEFT)
        self.assertEqual(carts[9].getPos(), (104, 73))

        self.assertEqual(carts[10].getDirection(), Cart.CART_DIR_DOWN)
        self.assertEqual(carts[10].getPos(), (33, 96))        

        self.assertEqual(carts[16].getDirection(), Cart.CART_DIR_DOWN)
        self.assertEqual(carts[16].getPos(), (143, 132))

        #total ticks 23
        self.tick(tracks, carts, 20)
        self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_UP)
        self.assertEqual(carts[0].getPos(), (41, 2))
        
        self.assertEqual(carts[9].getDirection(), Cart.CART_DIR_LEFT)
        self.assertEqual(carts[9].getPos(), (88, 69))

        self.assertEqual(carts[10].getDirection(), Cart.CART_DIR_DOWN)
        self.assertEqual(carts[10].getPos(), (27, 110))  

        self.assertEqual(carts[16].getDirection(), Cart.CART_DIR_LEFT)
        self.assertEqual(carts[16].getPos(), (135, 144))

        #total ticks 24
        self.tick(tracks, carts, 1)
        self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_RIGHT)
        self.assertEqual(carts[0].getPos(), (41, 1))

        self.assertEqual(carts[10].getDirection(), Cart.CART_DIR_DOWN)
        self.assertEqual(carts[10].getPos(), (27, 111))  

        self.assertEqual(carts[16].getDirection(), Cart.CART_DIR_LEFT)
        self.assertEqual(carts[16].getPos(), (134, 144))
        
       





if __name__ == '__main__':
    unittest.main()