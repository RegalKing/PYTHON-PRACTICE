
import time

# ---------------------------------------

n=10
for i in range (n,20): # first number is INCLUSE last number is EXCLUSIVE, if you want to include the last number add +1, so 20+1
    print ("="+str(i))
print()

for i in range (n,20+1,2): # the THIRD argument of a for loop is a STEP
    print ("=="+str(i))
print()

for i in "Alexxxx":
    print ("==="+str(i))

# ---------------------------------------

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year!")
