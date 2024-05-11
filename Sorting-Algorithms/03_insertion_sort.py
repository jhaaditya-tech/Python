def insertion_sort(list):
    for i in range(1, len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    print(list)

clist=[5,9,7,3,2,73,89,87]
insertion_sort(clist)   
            
        
            