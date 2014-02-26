ls=open("in.txt").readlines()
r=[]
for l in ls[:-1]:
    r.append(l[:-2])
r.append(ls[-1])
f=open("out.txt","w")
f.write(" ".join(r))
f.close()

