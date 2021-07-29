#!/usr/bin/env python
from typing import Counter


x= [2,2,2,2,4,4,4,5,5,5,1,1,1,1,3,3]
q = Counter(sorted(x))
print(sum(s for s in q.values))
print(q.most_common(1)[0][0])
print(x)