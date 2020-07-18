import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    Alice=0
    Bob=0
    result=[]
    for i in range(len(a)):
        if(a[i]>b[i]):
            Alice+=1
        elif(a[i]<b[i]):
            Bob+=1
        else :
            pass 
    result.append(Alice)
    result.append(Bob)
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()