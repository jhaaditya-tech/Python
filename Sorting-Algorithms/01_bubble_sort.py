def bubble_sort(custom_list):
    for i in range(len(custom_list)-1):
        swapped=False
        for j in range(len(custom_list)-i-1):
            if custom_list[j]>custom_list[j+1]:
                custom_list[j],custom_list[j+1]=custom_list[j+1],custom_list[j]
                swapped=True
        if not swapped:
            break
    print(custom_list)

clist=[5,9,7,3,2,73,89,87]
bubble_sort(clist)
                
        