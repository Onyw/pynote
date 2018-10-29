import pickle
f=open(r'f:\python代码\123.txt','wb')
n=1
a={'jfb':99,'cz':99}
pickle.dump(n,f)
pickle.dump(a,f)
f.close()
f=open(r'f:\python代码\123.txt','rb')
n=pickle.load(f)
i=1
while i<=n:
    temp=pickle.load(f)
    print(temp)
    i+=1
f.close()