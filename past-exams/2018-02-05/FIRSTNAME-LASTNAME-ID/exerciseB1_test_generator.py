"""
Generates testcases for exerciseB1
"""

import random
from exerciseB1 import *

random.seed(0)

def print_big():
		# print(subsetsum([2,5,4,3,12], 9))
		# print(subsetsum([2,5,4,3,12], 25))
		#
		ntests = 20
		for i in range(ntests):
				size = random.randint(20,30)
				A = []
				for k in range(size):
						A.append(random.randint(4,size*10))
				S = random.randint(size*size, size*size*10)
				print("self.assertEqual(subsetsum(",A,",",S,"), ", subsetsum(A,S),")", sep="")

def print_small():
		levels = 5
		level_reps = 3
		res = set([])
		for level in range(1, levels):
				for level_rep in range(level_reps):
						A = []
						for x in range(level):
								A.append(random.randint(0,5))

						for z in range(1, level+1):
								S = 0
								B = A.copy()
								for y in range(1,z+1):
										i = random.randint(0, len(B)-1)
										S += B.pop(i)
								res.add((tuple(A), S))
								S2 = S + random.randint(1,3)
								res.add((tuple(A), S2))
		reslist = list(res)
		import functools
		reslist = sorted(reslist, key=functools.cmp_to_key(lambda t1,t2:(len(t1[0]) - len(t2[0]))))
		for (A, S) in reslist:
				print("self.assertEqual(subsetsum(",list(A),",",S,"), ", subsetsum(A,S),")", sep="")


		#        self.assertEquals(squares(0),0)

print_small()
print_big()