import unittest
from exerciseB1 import *


class SubsetSumTest(unittest.TestCase):

    def test_neg(self):
        self.assertEqual(subsetsum([],-1), False)
        self.assertEqual(subsetsum([1],-1), False)

    def test_0(self):
        self.assertEqual(subsetsum([],0),True)
        self.assertEqual(subsetsum([1],0),True)

    def test_1(self):
        self.assertEqual(subsetsum([3],4), False)
        self.assertEqual(subsetsum([2],2), True)
        self.assertEqual(subsetsum([3],3), True)
        self.assertEqual(subsetsum([2],4), False)

    def test_2(self):
        self.assertEqual(subsetsum([2, 3],5), True)
        self.assertEqual(subsetsum([4, 1],4), True)
        self.assertEqual(subsetsum([2, 3],2), True)
        self.assertEqual(subsetsum([4, 1],8), False)
        self.assertEqual(subsetsum([2, 4],2), True)
        self.assertEqual(subsetsum([4, 1],5), True)
        self.assertEqual(subsetsum([2, 4],6), True)
        self.assertEqual(subsetsum([2, 3],8), False)
        self.assertEqual(subsetsum([4, 1],6), False)
        self.assertEqual(subsetsum([2, 4],9), False)
        self.assertEqual(subsetsum([2, 4],4), True)
        self.assertEqual(subsetsum([2, 3],4), False)

    def test_3(self):
        self.assertEqual(subsetsum([3, 5, 5],5), True)
        self.assertEqual(subsetsum([5, 1, 4],5), True)
        self.assertEqual(subsetsum([4, 1, 1],4), True)
        self.assertEqual(subsetsum([5, 1, 4],1), True)
        self.assertEqual(subsetsum([3, 5, 5],13), True)
        self.assertEqual(subsetsum([3, 5, 5],6), False)
        self.assertEqual(subsetsum([3, 5, 5],10), True)
        self.assertEqual(subsetsum([3, 5, 5],14), False)
        self.assertEqual(subsetsum([4, 1, 1],7), False)
        self.assertEqual(subsetsum([4, 1, 1],6), True)
        self.assertEqual(subsetsum([5, 1, 4],3), False)
        self.assertEqual(subsetsum([3, 5, 5],12), False)
        self.assertEqual(subsetsum([5, 1, 4],10), True)
        self.assertEqual(subsetsum([5, 1, 4],6), True)
        self.assertEqual(subsetsum([4, 1, 1],8), False)
        self.assertEqual(subsetsum([5, 1, 4],13), False)
        self.assertEqual(subsetsum([4, 1, 1],5), True)

    def test_3(self):
        self.assertEqual(subsetsum([4, 2, 5, 0],5), True)
        self.assertEqual(subsetsum([5, 4, 3, 4],3), True)
        self.assertEqual(subsetsum([5, 4, 3, 4],12), True)
        self.assertEqual(subsetsum([5, 4, 3, 4],7), True)
        self.assertEqual(subsetsum([4, 2, 5, 0],2), True)
        self.assertEqual(subsetsum([4, 2, 5, 0],12), False)
        self.assertEqual(subsetsum([5, 4, 3, 4],16), True)
        self.assertEqual(subsetsum([1, 1, 0, 4],3), False)
        self.assertEqual(subsetsum([5, 4, 3, 4],15), False)
        self.assertEqual(subsetsum([1, 1, 0, 4],7), False)
        self.assertEqual(subsetsum([4, 2, 5, 0],14), False)
        self.assertEqual(subsetsum([5, 4, 3, 4],10), False)
        self.assertEqual(subsetsum([1, 1, 0, 4],2), True)
        self.assertEqual(subsetsum([5, 4, 3, 4],17), False)
        self.assertEqual(subsetsum([4, 2, 5, 0],11), True)
        self.assertEqual(subsetsum([1, 1, 0, 4],6), True)
        self.assertEqual(subsetsum([5, 4, 3, 4],5), True)
        self.assertEqual(subsetsum([1, 1, 0, 4],5), True)
        self.assertEqual(subsetsum([4, 2, 5, 0],8), False)
        self.assertEqual(subsetsum([1, 1, 0, 4],0), True)


    def test_many(self):
        self.assertEqual(subsetsum([242, 189, 35, 135, 169, 126, 211, 177, 219, 190, 259, 246, 134, 106, 11, 50, 4, 149, 228, 161, 159, 123, 257, 130, 191, 254],2901), True)
        self.assertEqual(subsetsum([156, 141, 95, 192, 83, 140, 153, 34, 139, 129, 8, 181, 141, 194, 158, 92, 122, 61, 119, 198],2699), False)
        self.assertEqual(subsetsum([200, 85, 22, 30, 47, 152, 205, 20, 148, 10, 38, 77, 185, 142, 200, 30, 177, 167, 142, 140, 189, 172, 96],3093), False)
        self.assertEqual(subsetsum([133, 4, 144, 35, 50, 152, 81, 210, 185, 36, 31, 153, 6, 111, 198, 218, 46, 32, 227, 237, 27, 116, 110, 211],2470), True)
        self.assertEqual(subsetsum([80, 27, 118, 94, 143, 204, 145, 81, 56, 10, 200, 165, 189, 209, 166, 38, 157, 162, 46, 126, 179],4236), False)
        self.assertEqual(subsetsum([7, 27, 130, 34, 29, 194, 131, 23, 73, 55, 63, 179, 52, 185, 73, 51, 196, 196, 157, 109, 163, 197],4052), False)
        self.assertEqual(subsetsum([14, 263, 99, 218, 79, 64, 109, 249, 23, 73, 21, 257, 129, 228, 112, 193, 97, 25, 136, 272, 34, 22, 261, 263, 220, 25, 157, 235, 159],7719), False)
        self.assertEqual(subsetsum([31, 56, 137, 132, 50, 13, 185, 150, 88, 67, 200, 78, 152, 84, 67, 21, 257, 61, 247, 107, 260, 7, 4, 216, 116, 16, 198, 5, 107, 143],1667), True)
        self.assertEqual(subsetsum([196, 204, 170, 32, 231, 34, 220, 226, 8, 9, 75, 37, 75, 146, 104, 240, 82, 224, 23, 202, 34, 97, 92, 223],3155), False)
        self.assertEqual(subsetsum([202, 138, 72, 54, 113, 9, 80, 93, 225, 188, 111, 160, 185, 225, 39, 91, 154, 6, 178, 84, 250, 56, 175, 82, 57],5457), False)
        self.assertEqual(subsetsum([169, 225, 157, 135, 213, 258, 68, 284, 97, 39, 232, 107, 266, 30, 175, 235, 129, 34, 181, 15, 7, 253, 221, 244, 56, 45, 220, 95, 173],1063), True)
        self.assertEqual(subsetsum([65, 172, 81, 34, 198, 6, 113, 57, 113, 187, 118, 61, 42, 157, 137, 112, 17, 179, 21, 168],3041), False)
        self.assertEqual(subsetsum([144, 64, 120, 30, 20, 26, 42, 72, 145, 199, 131, 205, 111, 104, 10, 88, 55, 185, 192, 109, 37],3733), False)
        self.assertEqual(subsetsum([6, 75, 61, 21, 161, 9, 137, 73, 113, 157, 168, 77, 54, 5, 27, 33, 150, 80, 45, 49, 54, 33],798), True)
        self.assertEqual(subsetsum([27, 200, 83, 27, 57, 59, 67, 223, 111, 162, 59, 136, 84, 150, 200, 144, 82, 132, 193, 166, 74, 81, 115, 28],701), True)
        self.assertEqual(subsetsum([213, 159, 108, 172, 32, 187, 193, 114, 163, 115, 107, 30, 120, 250, 57, 92, 57, 162, 27, 230, 56, 61, 90, 105, 56, 208],5165), False)
        self.assertEqual(subsetsum([18, 125, 222, 195, 291, 198, 150, 105, 145, 224, 280, 226, 68, 173, 171, 11, 282, 136, 187, 194, 67, 262, 35, 98, 180, 215, 107, 19, 272, 162],1153), True)
        self.assertEqual(subsetsum([121, 273, 191, 47, 92, 202, 38, 162, 276, 229, 180, 225, 224, 113, 275, 58, 52, 61, 275, 262, 149, 147, 217, 107, 60, 60, 49, 14],1118), True)
        self.assertEqual(subsetsum([70, 148, 45, 58, 155, 124, 106, 24, 113, 121, 41, 99, 146, 63, 21, 40, 192, 78, 193, 120],3099), False)
        self.assertEqual(subsetsum([258, 253, 124, 83, 231, 88, 17, 85, 215, 175, 21, 107, 166, 78, 132, 241, 122, 42, 221, 73, 38, 37, 146, 56, 154, 257],2158), True)


