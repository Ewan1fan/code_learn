print(([[val,key] for key,val in enumerate([2,1,1,1,1,2,2,3])]))
print(sorted([[val,key] for key,val in enumerate([2,1,1,1,1,2,2,3])]))
print([val for key,val in enumerate([2,1,1,1,1,2,2,3])].count(1))
a = {1,2,3,4}
print(list(a))
print([a])
b = ['b','a','c']
print(set(b))
for [a,b] in [[1,2]]:
    print(a)

print([1]*5)
# ac = 'abc'
# ac[1] = 'v'
print(2%10)
row,col = divmod(80,9)
print(row,col)
# print([1,2,3].sum())
a=[[0]*5 for _ in range(5)]
a[0][0]=1
print(a)