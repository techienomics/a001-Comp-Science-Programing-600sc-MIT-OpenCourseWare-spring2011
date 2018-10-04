###Find the cube root of a perfect cube
##x = int(input('Enter an integer: '))
##ans = 0
##while ans*ans*ans < abs(x):
##    ans = ans + 1
##    print ('current guess =', ans)
##if ans*ans*ans != abs(x):
##    print (x, 'is not a perfect cube')
##else:
##    if x < 0:
##        ans = -ans
##    print ('Cube root of ' + str(x) + ' is ' + str(ans))

###Find the cube root of a perfect cube
##x = int(input('Enter an integer: '))
##for ans in range(0, abs(x)+1):
##    #print ('current guess =', ans)
##    if ans**3 == abs(x):
##        break
##if ans**3 != abs(x):
##    print (x, 'is not a perfect cube')
##else:
##    if x < 0:
##        ans = -ans
##    print ('Cube root of ' + str(x) + ' is ' + str(ans))

### approximation example, brute force with optimization
##x = int(input('Enter an integer: '))            # x = 25
##epsilon = 0.01
##numGuesses = 0
##ans = 0.0
##while abs(ans**2 - x) >= epsilon and ans <= x:
##    ans += 0.00001
##    numGuesses += 1
##print ('numGuesses =', numGuesses)
##if abs(ans**2 - x) >= epsilon:
##    print ('Failed on square root of', x)
##else:
##    print (ans, 'is close to square root of', x)

### approximation example, brute force with bisection search (divide and conquer)
##x = float(input('Enter a float: '))             #x = 12345, x = 0.5 explote :)
##epsilon = 0.01
##numGuesses = 0
##low = 0.0
##high = max(x,1)                                 #max(x,1) instead high = x solve 0 to 1 flaw
##ans = (high + low)/2.0
##while abs(ans**2 - x) >= epsilon and ans <= x:
##    print (low, high, ans)
##    numGuesses += 1
##    if ans**2 < x:
##        low = ans
##    else:
##        high = ans
##    ans = (high + low)/2.0
##print ('numGuesses =', numGuesses)
##print (ans, 'is close to square root of', x)

### function example, abstraction and decomposition
##def withinEpsilon(x, y, epsilon):
##    """x, y, epsilon all ints or floats
##       returns true if x is within epsilon of y"""
##    return abs(x - y) <= epsilon
##
##if withinEpsilon(25, 26, 1):
##    print ('yes')
##else:
##    print ('no')
##
##if withinEpsilon(25, 26, 0.9):
##    print ('yes')
##else:
##    print ('no')

