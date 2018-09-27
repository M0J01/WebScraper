
list1 = ['pinapples','pinapples','pinapples','pinapples','Tomatoe']
list2 = ['pinapples','pinapples','pinapples','Tomatoe']
list3 = ['pinapples','pinapples','Tomatoe']

newlist = []
newlist.append(list1)
newlist.append(list3)
newlist.append(list2)

doneList = []



for i in range(len(newlist)):
    item = newlist.pop()
    if item not in doneList:
        doneList.append(item)

newlist.append(['Brassberrys','pinapples','Tomatoe'])

for i in range(len(newlist)):
    item = newlist.pop()
    if item not in doneList:
        doneList.append(item)


[print(item, '\n') for item in doneList]
print("donelist")
[print(item, '\n') for item in newlist]

fname = 'phile.txt'
f = open(fname, 'a')
[f.write(str(item) + '\n') for item in doneList]
f.close()

