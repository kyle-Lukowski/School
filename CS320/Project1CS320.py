def listprimeshelper(n, i=2):
    if n == 2: 
        return True
    if n == 1: 
        return False
    if n % i == 0: #not prime if remainder is 0
        return False
    if i * i > n:
        return True
    return listprimeshelper(n, i+1)

def listPrimesBelow(n, primelist, i):

    if i < 2:
            return primelist
    if listprimeshelper(i): #if prime add number to primelist and decrease n by 1
            primelist.append(i)

    return listPrimesBelow(n, primelist, i-1) #i is the current number being checked if prime




def isBst(list, min_val=float('-inf'), max_val=float('inf')):
    if len(list) == 0: #base case if list is empty then true as the lower condition never triggered
       return True

    current = list[0] 
    leftchild = list[1]
    rightchild = list[2]

    if (min_val > current or current > max_val): #checks bst properties are still maintained false if not
        return False

    return isBst(leftchild, min_val, current) and isBst(rightchild, current, max_val)


def Main():
    #list primes test
    primelist = []
    n = 30
    print(listPrimesBelow(n, primelist, n-1))

#Binary Search Tree tests
    tests = [
    [4, [2, [1, [], []], [3, [], []]], [6, [5, [], []], []]], # t
    [4, [2, [1, [], []], [3, [], []]], [6, [9, [], []], []]], # f
    [4, [2, [1, [], []], [3, [], []]], [1, [5, [], []], []]], # f
    [4, [7, [1, [], []], [3, [], []]], [6, [5, [], []], []]], # f
    [4, [2, [1, [], []], [1, [], []]], [6, [5, [], []], []]], # f
    [4, [2, [4, [], []], [3, [], []]], [6, [5, [], []], []]], # f
    [4, [2, [1, [], []], [3, [], []]], [6, [], [9, [], []]]]] # t


    for i in range(0, len(tests)):
        print(f"Test Case {i + 1}: {isBst(tests[i])}")


    

Main()
    