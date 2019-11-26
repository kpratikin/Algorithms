'''
Created on Nov 11, 2019

@author: Pratik
'''

lst = [5, 8, 5, 2]
#lst = [5, 8, 5, 2, 9,1,6,8,9,6,7]

def bubble_pratik(lst):
    last = len(lst)
    while (last>0):
        for i in range(0,last):  
            #for j in range(i+1, len(lst)):
            if i+1<last:
                if lst[i]>lst[i+1]:
                    tmp = lst[i]
                    lst[i] = lst[i+1]
                    lst[i+1]=tmp
        last-=1
    return(lst)

def bubble_geek(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):  
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]  = lst[j+1], lst[j]
    return(lst)

print(bubble_geek(lst))
print(bubble_pratik(lst))
