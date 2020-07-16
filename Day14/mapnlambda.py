cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    n1,n2=0,1
    l=[]
    # return a list of fibonacci numbers
    for i in range(0,n):
        l.append(n1)
        k=n1+n2
        n1=n2
        n2=k
    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))