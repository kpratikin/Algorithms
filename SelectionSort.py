#Selection Sort
lst = [5, 8, 5, 2, 9,1,6,8,9,6,7]
#lst = [5, 8, 5, 2]

def findsmallest(a):
    smallest = a[0]
    smallest_index = 0
    for j in range(0, (len(a))):
        #print('j=%s'%j)
        if a[j]<smallest:
            smallest=a[j]
            smallest_index=j
    return smallest_index


for i in range (0, (len(lst))):
    #print('i=%s'%i)
    smallest_index = findsmallest(lst[i:])+i
    #replace
    tmp = lst[i]
    lst[i] = lst[smallest_index]
    lst[smallest_index] = tmp
     
#for i in range(0, len(lst)):
#    for j in range(i, len(lst)):
#        if lst[j]<lst[i]:
#            tmp = lst[j]
#            lst[j] = lst[i]
#            lst[i] = tmp

print(lst)
    