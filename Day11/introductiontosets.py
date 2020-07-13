def average(array):
    # your code goes here
    array=set(array)
    sum=0
    count=0
    for i in array:
        sum=sum+i
        count=count+1
    av=sum/count
    return av
    '''return sum(set(array))/len(set(array))'''


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)