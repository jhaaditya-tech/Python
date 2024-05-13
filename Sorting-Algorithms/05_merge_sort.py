def merge(left,right):
    sorted_array=[]
    left_index=0
    right_index=0
    
    #Compare element from left and right order and merge them in sorted order
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            sorted_array.append(left[left_index])
            left_index+=1
        else:
            sorted_array.append(right[right_index])
            right_index+=1
    
    #If there are remaining elements in the left array add them
    while left_index<len(left):
        sorted_array.append(left[left_index])
        left_index+=1
        
    #If there are reaming elements in the right array, add them
    while right_index<len(right):
        sorted_array.append(right[right_index])
        right_index+=1
    
    return sorted_array


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    #Dividing the array into two halves
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    
    #Recurseively sort both array
    left_sorted=merge_sort(left_half)
    right_sorted=merge_sort(right_half)
    
    #Merge the sorted halves
    return merge(left_sorted,right_sorted)


clist=[5,9,7,3,2,73,89,87]
print(merge_sort(clist))  



        
    