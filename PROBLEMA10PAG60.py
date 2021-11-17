import itertools
multimea={1,2,3,4}
for i in range(len(multimea)):
    submultime=itertools.combinations(multimea, i+1)
    print(set(submultime))