
name = "William W. Warhawk" #1

print(name[0:7])  #2 "William"
print(name[11:18]) # "Warhawk"
print(name[14:18]) #  "hawk"
print(name[5:7])  # "am"
print(name[1:4])  # "ill"

numlist = [10, 20, 40, 80,] #3 Define list with given numbers
numlist.append(60) #4 append list with 60
numlist.remove(10) #5 remove 10 from list

for i in numlist: #loop without range
    print(i)


for i in range(len(numlist)):  #loop with range
    print(numlist[i])

    



