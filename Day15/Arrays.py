mport numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    result=numpy.array(arr,float)
    result=numpy.flipud(result)
    
    return result

arr = input().strip().split(' ')
result = arrays(arr)
print(result)