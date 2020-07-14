from itertools import combinations_with_replacement

l=input()
l1=l.split(' ')


for c in combinations_with_replacement(sorted(l1[0]), int(l1[1])):
    print("".join(c))