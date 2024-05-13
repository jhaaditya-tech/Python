import math as m

def insertion_sort(list):
    for i in range(len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    return list
    
def bucket_sort(list):
    number_of_buckets=round(m.sqrt(len(list)))
    minValue=min(list)
    maxValue=max(list)
    rangeVal=(maxValue-minValue)/number_of_buckets

    buckets=[[] for _ in range(number_of_buckets)]
    
    for j in list:
        if j==maxValue:
            buckets[-1].append(j)
        else:
            index_b=m.floor((j-minValue)/rangeVal)
            buckets[index_b].append(j)
    
    sorted_array=[]
    for i in range(number_of_buckets):
        buckets[i]=insertion_sort(buckets[i])
        sorted_array.extend(buckets[i])
        
    return sorted_array

clist=[5,9,7,3,2,73,89,87]
print(bucket_sort(clist))  