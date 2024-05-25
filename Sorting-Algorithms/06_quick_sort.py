def quick_sort(arr, low, high):
    if low<high:
        #Partition the array and get the pivot index
        pi=partition(arr, low, high)
        
        #Recursively apply quick sort to the sub array
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
        

def partition(arr, low, high):
    #Use median-of-three stratehy to choose the pivot
    mid=(low+high)//2
    pivot=median_of_three(arr, low, mid, high)
    
    #Move the pivot to the end
    arr[high], arr[pivot]=arr[pivot], arr[high]
    pivot=arr[high]
    
    i=low-1 #Index of smaller element
    
    for j in range(low, high):
        #If the current element is smaller than or equal to the piot
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i] #Swap elements
            
    #Swap the pivot elements with the element at i+1
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def median_of_three(arr, low, mid, high):
    #Return the index of the median of arr[low], arr[mid], arr[high]
    if arr[low]<arr[mid]:
        if arr[mid]<arr[high]:
            return mid
        elif arr[low]<arr[high]:
            return high
        else:
            return low
    else:
        if arr[low]<arr[high]:
            return low
        elif arr[mid]<arr[high]:
            return high
        else:
            return mid
        
arr = [5, 9, 7, 3, 2, 73, 89, 87]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)

"""

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    #Choosing the middle element (middle element for simplicity)
    pivot=arr[len(arr)//2]
    
    #Partitioning array into three lists:
    #less (elements less than the pivot), equal (elements equal to the pivot), and greater (elemets greater than the pivot)
    less=[x for x in arr if x<pivot]
    equal=[x for x in arr if x==pivot]
    greater=[x for x in arr if x>pivot]
    
    return quick_sort(less)+equal+quick_sort(greater)

arr=[5,9,7,3,2,73,89,87]
sorted_arr=quick_sort(arr)
print("Sorted Array: ", sorted_arr)

"""
