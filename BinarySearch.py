'''
Created on Nov 12, 2019

@author: Pratik
'''

def binarysearch_pratik(lst, item):
    low=0
    high= len(lst)-1
    
    while low<=high:
        mid = int((low+high)/2)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    
    return None 
        
        

lst = [1,2,3,5,9,10,15,20]

print(binarysearch_pratik(lst,15))

