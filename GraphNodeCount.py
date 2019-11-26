'''
Created on Nov 14, 2019

@author: Pratik
'''
from collections import deque
graph = {}
graph['start']=['a','b']
graph['a']=['c','e']
graph['b']=['e']
graph['c']=['d']
graph['e']=['c','a']
graph['d']=[]

visited = []
node_count =0

search_que = deque()
search_que += graph['start']

while search_que:
    node = search_que.popleft()
    if node not in visited:
            #Count and Extract and deque
        node_count+=1
        search_que+=graph[node]
        visited.append(node)
            

print(node_count+1)
            
    
        
    
        