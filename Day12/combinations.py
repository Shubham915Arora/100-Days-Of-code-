# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a=input()

l=a.split(' ')

print(*[''.join(i) for i in permutations(sorted(l[0]),int(l[1]))],sep='\n')