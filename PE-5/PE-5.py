from itertools import count

#from 20 and up multiply, when it all factors, break
for i in count(20, 20): # has to be divisable by 20 anyways, so increase by 20
    if all(map(lambda x: i % x == 0, range(10, 21))):
        print(i)
        break

# brute force, I feel like I can get an elegant solution in using prime factors but I'm not quite sure how
