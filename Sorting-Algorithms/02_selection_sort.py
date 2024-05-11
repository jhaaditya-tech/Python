def selection_sort(list):
    for i in range(len(list)):
        min_index=i
        for j in range(i+1, len(list)):
            if list[j]<list[min_index]:
                min_index=j
        list[min_index],list[i]=list[i],list[min_index]
    print(list)

clist=[5,9,7,3,2,73,89,87]
selection_sort(clist)   