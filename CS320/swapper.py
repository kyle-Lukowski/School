def swapper(s1, s2, l: list):
    for i in range(len(l)):
        if(l[i] == s1):
            l[i] = s2
        elif(l[i] == s2):
            l[i] = s1
    
    return l

def Main():

    list1 = [4,3,2,1]
    print("swapper test 1")
    print(swapper(4,6,list1))

    list2 = ["red", "green", "blue", "purple"]
    print("swapper test 2")
    print(swapper(3,"blue",list2))

    list3 = [1,2,3,1,2,2]
    print("swapper test 3")
    print(swapper(1,2,list3))


Main()