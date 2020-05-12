import math
import time

ans  = "1"	
for i in range(int(100000000),1000000000):
	ans  += str(i)
	start = time.time()
	print("Len : " + str(len(str(ans))) + "\n\n")
	print("Time taken : " + str(time.time()-start))

'''
start = time.time()
	print(str(int(math.log10(int(ans)) + 1)))
print("Time taken : " + str(time.time()-start))
'''