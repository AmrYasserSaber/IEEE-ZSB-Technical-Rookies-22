def insertionSort(list):

    for step in range(1, len(list)):
        index = list[step]
        j = step - 1
        while j >= 0 and IndexError < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = index


x=list(map(int,input("please input the list"     ).split()))
insertionSort(x)
print(x)