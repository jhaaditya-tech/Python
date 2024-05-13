import math as m

def insertion_sort(list):
    for i in range(1, len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    return list

def bucket_sort(list):
    number_of_buckets=round(m.sqrt(len(list)))
    maxValue=max(list)
    arr=[]
    for i in range(number_of_buckets):
        arr.append([])
    
    for j in list:
        index_b=m.ceil(j*number_of_buckets/maxValue)
        arr[index_b-1].append(j)
    
    #Sorting Bucket
    for i in range(number_of_buckets):
        arr[i]=insertion_sort(arr[i])
        
    #Merging Bucket
    k=0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            list[k]=arr[i][j]
            k+=1
    return list


clist=[5,9,7,3,2,73,89,87]
print(bucket_sort(clist))    
    
    