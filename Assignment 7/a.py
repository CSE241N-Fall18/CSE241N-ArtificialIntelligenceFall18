l = ['a' ,'v','c','d']
g = {'a':4 ,'v':44,'c':1,'d':3}
h = {'a':4 ,'v':44,'c':1,'d':3} 
l = sorted(l, key = lambda k : g[k]+h[k], reverse = False)
print(l)