def quickSort(myList):
    if len(myList) <= 1:
        return myList
    pivot = myList.pop()
    lessList = []
    moreList = []
    for item in myList:
        if item <= pivot:
            lessList.append(item)
        else:#item > myList           
            moreList.append(item)
    return quickSort(lessList)+[pivot] + quickSort(moreList)#make sure pivot in middle

def mergeSort(myList):
    lengthOfList = len(myList)
    if lengthOfList <=1:
        return myList
    return merge(mergeSort(myList[0:lengthOfList/2]),mergeSort(myList[lengthOfList/2:]))

def merge(list1,list2):
    mergedList = []
    while list1 and list2:   
        if list1[0] <= list2[0]:
            mergedList.append(list1.pop(0))#carefull with python implementation of pop and append
        else:
            mergedList.append(list2.pop(0))
    if list1:
        mergedList.extend(list1)
    if list2:
        mergedList.extend(list2)
    return mergedList

myList = [8,2,8,3,5,0,11,4,9]
print "Original List:"
print myList
print
print "Quick Sort:"
print quickSort(myList[:])
print
print "Merge Sort:"

print mergeSort(myList[:])
