def value_count(x, l: list[int]):
    
    count = 0
    for i in range(len(l)):
        if(x == l[i]):
            count = count + 1

    return count


def Main():

    list1 = [4,3,2,1]
    print("Value_count test 1:")
    print(value_count(1,list1))

    list2 = [1,2,3,1,2,2]
    print("Value_count test 2:")
    print(value_count(1,list2))

    list3 = [1,2,3,1,2,2]
    print("Value_count test 3:")
    print(value_count(2,list3))

    x = 3
    y = 4
    z = 1
    print (x + x * y - z)

Main()