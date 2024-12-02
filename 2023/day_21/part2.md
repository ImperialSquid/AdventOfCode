Many thanks to the users of the AoC subreddit for pointers in the right direction with this one!


BFS won't work for part 2 but we can make a few special observations 
First, The grid not olf has edges that allow uninterrupted travel, but it also has direct paths from the centre to the edge 
So, since the the grid width is 131, so the dict to an edge is 6

x1 = j = 65

x2 = j + k = 65 + 131

x3 = j + 2k = 65 + 131*2


y1 = a * x1^2 + b * x1 + c
   = a * j^2 + b * j + c

y2 = a * x2^2 + b * x2 + c
   = a * (j^2 + 2jk + k^2) + b * (j + k) + c

y3 = a * x3^2 + b * x3 + c
   = a * (j^2 + 4jk + 4k^2) + b * (j + 2k) + c



2 * y2 - y1 - y3
   = a * (2j^2 + 4jk + 2k^2)  + b * (2j + 2k) + 2c -
     a * j^2                  + b * j         + c  -
     a * (j^2 + 4jk + 4k^2)   + b * (j + 2k)  + c
   = a * ((2j^2 + 4jk + 2k^2) - j^2 - (j^2 + 4jk + 4k^2))
     a * -2k^2

a  = (2*y2 - y1 - y3) / -2k^2

y3 - y2
   = a * (j^2 + 4jk + 4k^2) + b * (j + 2k) + c -
     a * (j^2 + 2jk + k^2)  + b * (j + k)  + c  
   = a * (2jk + 3k^2)       + b * k

# a is known

b = (y3 - y2 - a * (2jk + 3k^2)) / k

# a and b are know

c = y1 - a * j^2 + b * j


XXXXX XXXXX XX3XX XXXXX XXXXX
XXXXX XXXXX X333X XXXXX XXXXX
XXXXX XXXXX 33333 XXXXX XXXXX
XXXXX XXXX3 33333 3XXXX XXXXX
XXXXX XXX33 33333 33XXX XXXXX

XXXXX XX333 33233 XXXXX XXXXX
XXXXX X3333 32223 3333X XXXXX
XXXXX 33333 22222 33333 XXXXX
XXXX3 33332 22222 23333 3XXXX
XXX33 33322 22222 22333 33XXX

XX333 33222 22122 22233 333XX
X3333 32222 21112 22223 3333X
33333 22222 11111 22222 33333
X3333 32222 X1112 22223 3333X
XX333 33222 22122 22233 333XX

XXX33 33322 22222 22333 33XXX
XXXX3 33332 22222 23333 3XXXX
XXXXX 33333 22222 33333 XXXXX
XXXXX X3333 32223 3333X XXXXX
XXXXX XX333 33233 333XX XXXXX

XXXXX XXX33 33333 33XXX XXXXX
XXXXX XXXX3 33333 3XXXX XXXXX
XXXXX XXXXX 33333 XXXXX XXXXX
XXXXX XXXXX X333X XXXXX XXXXX
XXXXX XXXXX XX3XX XXXXX XXXXX

