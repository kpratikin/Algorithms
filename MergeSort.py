'''
Created on Nov 11, 2019

@author: Pratik
'''
import math

#def merge(arr):

def mergesort_pratik(arr):
    #newarr= []
    n = len(arr)
    #Base Case
    if n<2:
        #merge
        return arr
    # Recursive Case
    else:
        #divide
        mid = math.floor(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]
        mergesort_pratik(left)
        mergesort_pratik(right)
        
        i= j= k= 0
        while i< len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k] =left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    
    return arr

lst = [5, 8, 5, 2]
#lst = [5, 8, 5, 2, 9,1,6,8,9,6,7]
print(mergesort_pratik(lst))