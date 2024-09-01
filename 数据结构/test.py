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
a=[[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
a.sort(key=lambda x:(x[0],x[1]))
print(a)
b=[[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
b.sort(key=lambda x:x[0])
print(b)
print(len('qwertyuiopasdfghjklzxcvbnm'))
print(ord('a'))
a = {'a','b'}
a.add('a')
print(a)
print('d' in 'abc')
print(int('01'))
print('0'>'8')
print('8'>'11')
print(list(str(123)))

# n, m = map(int, input().split( ))
# graph = [[0] * (n + 1) for _ in range(n + 1)]

# for _ in range(m):
#     s, t = map(int, input().split( ))
#     graph[s][t] = 1
# print(graph)

print(type(30/2))
print(type(30//2))
print([[[]]*(2) for _ in range(2)])
print(max('00','0',key = lambda x:len(x)))
print(len([]))
dp = [[[]]*(2) for _ in range(2)]
print(len(dp[1][1]))