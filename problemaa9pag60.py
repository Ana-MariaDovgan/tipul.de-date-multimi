A = set(str(input('Dati multimea A:')))
B = set(str(input('Dati multimea B:')))
if (all(x.isupper() for x in A)) and (all(x.isupper() for x in B)) == True:
    print('Intersectia multimilor A si B -> ', A.intersection(B))
    print('Reuniunea multimilor A si B -> ', A.union(B))
    print('Diferenta multimilor A si B -> ', A.difference(B))
    print('Diferenta multimilor B si A -> ', B.difference(A))
else:
    print('Toate elementele trebuie sa fie litere mari')