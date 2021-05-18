p=input('enter a string=')
d={}
for x in p:
    if x in d:
        d[x]=d[x]+1
    else:
        d[x]=1
for i,j in d.items():
  print(i,'=',j)
