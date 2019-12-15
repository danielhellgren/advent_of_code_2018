import unittest
#import ../solution

#importing from parent dir in python........
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import solution

from cart import Cart

class RulesTest(unittest.TestCase):

    def init(self, filename):

        return solution.init(filename)

    def tick(self, tracks, carts, steps):
        for _ in range(steps):
            solution.moveCarts(tracks, carts)

    def test_loader(self):
        
        #check that init can handle subfolder
        tracks, carts = self.init("./test/test_intersection_input.txt")
        #CHECK INIT
        #amount of rows
        self.assertEqual(len(tracks), 3)
        #col
        self.assertEqual(len(tracks[0]), 6)
        #amount of carts loaded
        self.assertEqual(len(carts), 1)

    def test_turn(self):

        tracks, carts = self.init("./test/test_turn_input.txt")

        #intial positions
        self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_RIGHT)
        self.assertEqual(carts[0].getPos(), (1, 0))

        self.assertEqual(carts[1].getDirection(), Cart.CART_DIR_UP)
        self.assertEqual(carts[1].getPos(), (0, 1))

        self.assertEqual(carts[2].getDirection(), Cart.CART_DIR_DOWN)
        self.assertEqual(carts[2].getPos(), (2, 1))

        self.assertEqual(carts[3].getDirection(), Cart.CART_DIR_LEFT)
        self.assertEqual(carts[3].getPos(), (1, 2))

        #Given the inputs these carts should go around the track endlessly
        for tick in range(1000):

            #relative tick to get how many steps i the loop the cart should have gone
            relative_tick = tick % 8
            if relative_tick == 0:
                self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_RIGHT)
                self.assertEqual(carts[0].getPos(), (1, 0))

                self.assertEqual(carts[1].getDirection(), Cart.CART_DIR_UP)
                self.assertEqual(carts[1].getPos(), (0, 1))

                self.assertEqual(carts[2].getDirection(), Cart.CART_DIR_DOWN)
                self.assertEqual(carts[2].getPos(), (2, 1))

                self.assertEqual(carts[3].getDirection(), Cart.CART_DIR_LEFT)
                self.assertEqual(carts[3].getPos(), (1, 2))

            if relative_tick == 1:
                self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_DOWN)
                self.assertEqual(carts[0].getPos(), (2, 0))

                self.assertEqual(carts[1].getDirection(), Cart.CART_DIR_RIGHT)
                self.assertEqual(carts[1].getPos(), (0, 0))

                self.assertEqual(carts[2].getDirection(), Cart.CART_DIR_LEFT)
                self.assertEqual(carts[2].getPos(), (2, 2))

                self.assertEqual(carts[3].getDirection(), Cart.CART_DIR_UP)
                self.assertEqual(carts[3].getPos(), (0, 2))

            if relative_tick == 2:
                self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_DOWN)
                self.assertEqual(carts[0].getPos(), (2, 1))

                self.assertEqual(carts[1].getDirection(), Cart.CART_DIR_RIGHT)
                self.assertEqual(carts[1].getPos(), (1, 0))

                self.assertEqual(carts[2].getDirection(), Cart.CART_DIR_LEFT)
                self.assertEqual(carts[2].getPos(), (1, 2))

                self.assertEqual(carts[3].getDirection(), Cart.CART_DIR_UP)
                self.assertEqual(carts[3].getPos(), (0, 1))

            if relative_tick == 3:
                self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_LEFT)
                self.assertEqual(carts[0].getPos(), (2, 2))

                self.assertEqual(carts[1].getDirection(), Cart.CART_DIR_DOWN)
                self.assertEqual(carts[1].getPos(), (2, 0))

                self.assertEqual(carts[2].getDirection(), Cart.CART_DIR_UP)
                self.assertEqual(carts[2].getPos(), (0, 2))

                self.assertEqual(carts[3].getDirection(), Cart.CART_DIR_RIGHT)
                self.assertEqual(carts[3].getPos(), (0, 0))

            self.tick(tracks, carts, 1)

            



    def test_intersection(self):

        tracks, carts = self.init("./test/test_intersection_input.txt")

        #intial position
        self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_RIGHT)
        self.assertEqual(carts[0].getPos(), (1, 0))

        #given this input the cart should move around in a loop
        for tick in range(1000):

            #relative tick to get how many steps i the loop the cart should have gone
            relative_tick = tick % 12
            if relative_tick == 0:
                self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_RIGHT)
                self.assertEqual(carts[0].getPos(), (1, 0))
            if relative_tick == 1:
                self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_DOWN)
                self.assertEqual(carts[0].getPos(), (2, 0))
            if relative_tick == 2:
                self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_RIGHT)
                self.assertEqual(carts[0].getPos(), (2, 1))
            if relative_tick == 3:
                self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_RIGHT)
                self.assertEqual(carts[0].getPos(), (3, 1))
            if relative_tick == 4:
                self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_DOWN)
                self.assertEqual(carts[0].getPos(), (4, 1))
            if relative_tick == 5:
                self.assertEqual(carts[0].getDirection(), Cart.CART_DIR_LEFT)
                self.assertEqual(carts[0].getPos(), (4, 2))
            

            self.tick(tracks, carts, 1)


if __name__ == '__main__':

    unittest.main()