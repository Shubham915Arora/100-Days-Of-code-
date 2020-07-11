if __name__ == '__main__':
    n = int(input())
    a=input()
    input_list=a.split()
    for i in range(n):
        input_list[i]=int(input_list[i])

    t=tuple(input_list)

    print(hash(t))