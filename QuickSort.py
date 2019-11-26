'''
Created on Nov 11, 2019

@author: Pratik
'''

def quicksort_pratik(arr):
    n = len(arr)
    if n<=1:
        #exit
        return arr
    else:
        left=[]
        right=[]
        pivot = arr[0]
        i=1
        #for i in arr: left.append(i) if (i<pivot) else right.append(i)
        while i<n: 
            if (arr[i]<=pivot):
                left.append(arr[i])
            else:
                right.append(arr[i]) 
            i+=1
        
        sorted_left = quicksort_pratik(left)
        sorted_right = quicksort_pratik(right)
    return sorted_left+[pivot]+sorted_right
        
    
def quicksort_grokking(array):
    if len(array) < 2:
        # base case, arrays with 0 or 1 element are already "sorted"
        return array
    else:
        # recursive case
        pivot = array[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
    return quicksort_grokking(less) + [pivot] + quicksort_grokking(greater)

lst = [5, 8, 5, 2]
print(quicksort_pratik(lst))
print(quicksort_grokking(lst))

test = [i for i in range(0, 5) if i%2==0]
print(test)