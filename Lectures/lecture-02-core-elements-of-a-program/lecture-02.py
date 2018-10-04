### hello Phyton!
##
##x = 3                           #Ctrl+3 to comments, Ctrl+4 go back to scrip 
##print (x)                       # print() now use ()
##x = x*x                         #Bind x to value 9
##print (x)
##y = input('enter a number:')    #raw_input was renamed to just input
##print (type(y))
##print (y)
##y = float(input('Enter a number: '))
##print (type(y))
##print ('This is the value of y= ' + str(y))
##print (y*y)

### example 1 of a branching program
##
##x = int(input('Enter an integer: '))
##if x%2 == 0:
##    print ('Even')
##else:
##    print ('Odd')
##    if x%3 != 0:
##        print ('And not divisible by 3')


### example 2 of a branching program
##
##x = int(input('Enter x: '))
##y = int(input('Enter y: '))
##z = int(input('Enter z: '))
##
##print('Version using if else:')
##if x < y:
##    if x < z:
##        print ('x is least')
##    else:
##        print ('z is least')
##else:
##    print ('y is least')
##
##print('Version using if elif else:')
##if x < y:
##    if x < z:
##        print ('x is least')
##    else:
##        print ('z is least')
##elif y < z:
##    print ('y is least')
##else:
##    print ('z is least')
##
##if x < y and x < z:
##    print 'x is least'
##elif y < z:
##    print 'y is least'
##else:
##    print 'z is least'

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
