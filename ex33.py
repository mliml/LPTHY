j = 0
numbers = []

def test(q,i):
    while i < q:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


test(9,j)
print "The numbers:"

for num in numbers:
    print num
