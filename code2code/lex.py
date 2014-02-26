def getId(s):
	ds=s.split("=")
	if len(ds)==2:
		return ds[1]
	else:
		return s[1:][:-1]
s=open("AS3_ex.tokens").readlines()
dic1={}
dic2={}
for s1 in s:
	d=s1[:-1].split("=")
	if	len(d)==2:
		(k,v)=d
		dic1[k]=v
		dic2[v]=k
	elif len(d)==3:
		(k1,k2,v)=d
		k=k1+"="+k2
		dic1[k]=v
		dic2[v]=k
	elif len(d)==4:
		dic1['==']=d[-1]
		dic2[d[-1]]='=='
	elif len(d)==5:
		dic1['===']=d[-1]
		dic2[d[-1]]='==='
src=open("src0/playerJeepController.as").read()
ls=open("player.lex.txt").readlines()
for l in ls:
	cs=l[:-1].split(",")
	d=cs[1].split(":")
	b=d[0]
	e=d[1]
	b=int(b)
	e=int(e.split("=")[0])
	id=getId(cs[-2])
	print "'"+src[b:e+1]+"'",id,dic2[id]
	
	

