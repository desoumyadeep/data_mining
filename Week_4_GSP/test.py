#!/usr/bin/env python
import itertools
itemset= ['also', 'area', 'best', 'cajun', 'food', 'fresh', 'good', 'great', 'ice', 'like', 'menu', 'monday', 'nice', 'night', 'old', 'order', 'place', 'see', 'special', 'thin', 'wet', 'whole', 'win', 'wing', 'would', 'year']
itemset_2 = ['also', 'area', 'best', 'cajun', 'food', 'fresh', 'good', 'great', 'ice', 'like', 'menu', 'monday', 'nice', 'night', 'old', 'order', 'place', 'see', 'special', 'thin', 'wet', 'whole', 'win', 'wing', 'would', 'year']
        
q = [i + " " + j for i in itemset for j in itemset_2]

print(q)


'''
for p in itertools.permutations(itemset,3):
    f = frozenset([(list(x))[0] for x in p])
    print(f)

for i in itemset:
    for j in itemset:
        if(len(i.union(j)) == 2):
            #print(i.union(j))
            pass
'''
#print(_joined_list)

'''
c = [('A', 'B', 'A', 'C'), ('A', 'C', 'A', 'B', 'A', 'B'), ('B', 'A', 'A', 'C', 'D'), ('A', 'B', 'A', 'C'), ('A', 'C', 'A', 'B', 'A', 'B'), ('B', 'A', 'A', 'C', 'D'), ('A', 'B', 'A', 'C'), ('A', 'C', 'A', 'B', 'A', 'B'), ('B', 'A', 'A', 'C', 'D'), ('A', 'B', 'A', 'C'), ('A', 'C', 'A', 'B', 'A', 'B'), ('B', 'A', 'A', 'C', 'D'), ('A', 'B', 'A', 'C'), ('A', 'C', 'A', 'B', 'A', 'B'), ('B', 'A', 'A', 'C', 'D'), ('A', 'B', 'A', 'C'), ('A', 'C', 'A', 'B', 'A', 'B'), ('B', 'A', 'A', 'C', 'D'), ('A', 'B', 'A', 'C'), ('A', 'C', 'A', 'B', 'A', 'B'), ('B', 'A', 'A', 'C', 'D'), ('A', 'B', 'A', 'C'), ('A', 'C', 'A', 'B', 'A', 'B'), ('B', 'A', 'A', 'C', 'D')]
#print(c)
k = 3
d = set()
m = []
for rec in c:
    for x in range(len(rec)):
        l = list(sorted(rec[x:x+k]))
        if len (l) == k:
            m.append(l)

    d = set(tuple(x) for x in m)

    print(d)   
'''    
