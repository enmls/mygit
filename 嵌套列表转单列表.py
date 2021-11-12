##A nested list goes to a single column table

a = [[1, 2], [3, 4], ["xaxa", "xsaxa"]]
t = []
[t.extend(i) for i in a]
print(t)
#out[1, 2, 3, 4, 'xaxa', 'xsaxa']

#or

from itertools import chain
print (list(chain(*a)))
#对数字无感,字符会被拆分

#or

import itertools
a = [[1,2,3],[4,5,6], [7], ["xssx","sac"]]
out = list(itertools.chain.from_iterable(a))
print(out)
##[1, 2, 3, 4, 5, 6, 7, 'xssx', 'sac']

#or

a=[[1,2],[3,[8,7],4],["xas","xaa"]]
print (sum(a,[]))
#out[1, 2, 3, [8, 7], 4, 'xas', 'xaa']
