
def rollDie():                              # returns a random int between 1 and 6
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print (result)

import pylab

##pylab.plot([1,2,3,4], [1,2,3,4])
##pylab.plot([1,4,2,3], [5,6,7,8])
##pylab.show()                              # pylab.show print chart and stop running the program

##pylab.figure(1)
##pylab.plot([1,2,3,4], [1,2,3,4])
##pylab.figure(2)
##pylab.plot([1,4,2,3], [5,6,7,8])
##pylab.savefig('firstSaved')
##pylab.figure(1)
##pylab.plot([5,6,7,10])
##pylab.savefig('secondSaved')
##pylab.show()

# interest calculation
principal = 10000                           #initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(values)

pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')

pylab.show()
