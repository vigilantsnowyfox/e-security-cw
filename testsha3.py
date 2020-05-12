#Author: Bruno Marchand
import sys
import sha3

data=sys.argv[1]
import time
start=time.time()
print("Time started:")
print(start)
for x in range(1,10001):
	s=sha3.sha3_224(data.encode('utf-8')).hexdigest()
#	print(s)

print("Looped: ", x)
end=time.time()
print("Total time",(end-start))
