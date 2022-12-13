def recursive_binary_search(list, target):
    if len(list) == 0: # stopping condition
        return False 
    else:
        midpoint = (len(list))//2
        
        if list[midpoint] == target: # stopping condition
            return True
        else:
            if list[midpoint] < target: # this is recursion, function that calls itself
                return recursive_binary_search(list[midpoint+1:], target) # stopping condition
            else:
                return recursive_binary_search(list[:midpoint], target)# stopping condition

def verify(result):
    print("Target found: ", result)
        
numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = result = recursive_binary_search(numbers, 6)
verify(result)