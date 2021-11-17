import itertools
m={1,2,3,4}
for i in range(len(m)):
    submultime=itertools.combinations(m, i+1)
    print(set(submultime))