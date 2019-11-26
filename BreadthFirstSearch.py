'''
Created on Nov 13, 2019

@author: Pratik
'''
#Shortest Path
from collections import deque
#Mango seller

graph={}
graph['you'] = ['bob','claire','alice']
graph['bob'] = ['anuj','peggy']
graph['claire'] = ['thom','jonny']
graph['alice'] = ['peggy']
graph['anuj'] = []
graph['thom'] = []
graph['jonny'] = []
graph['peggy'] = []

def person_is_seller(name):
        print(name)
        return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue+=graph[name]
    searched=[]
    
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print('mango seller is %s'%person)
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False

print(search('you'))