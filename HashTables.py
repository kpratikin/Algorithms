'''
Created on Oct 25, 2019

@author: Pratik
'''

#Check if someone has already voted

voted_dict = {'tom':True, 'mummy':True,'pratik':True}

def fun_check_voted(name):

    if voted_dict.get(name):
        return 'Kick him'
    else:
        voted_dict[name]=True
        return 'Let him vote'
    
print(fun_check_voted('tom'))
print(fun_check_voted('ashwita'))
print(fun_check_voted('prinal'))
print(fun_check_voted('shruti'))


    
    
        