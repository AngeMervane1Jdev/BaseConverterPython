#coding-utf8
def deux_16(l,Tuple):
	n1,cpt,L,resultat=l,0,[],[]
	l=list(l)
	l.reverse()
	for t in l:
		L.append(int(t))
	if len(L)%4!=0:
		while cpt<len(L)%4:
			L.append(0)
			cpt+=1
	i=0
	while i<len(L):
		res=L[i]+L[i+1]*2+L[i+2]*4+L[i+3]*8
		if res>=10:
			for t,v in Tuple.items():
				if v==res:
					resultat.append(t)
		else:
			resultat.append(res)
		i+=4
	resultat.reverse()
	resultat=''.join(resultat)
	return resultat

def deux_8(l):
	n1=l
	L,resultat,cpt=[],[],0
	l.reverse()
	for t in l:
		L.append(int(t))
	if len(L)%3!=0:
		while cpt<len(L)%3:
			L.append(0)
			cpt+=1
	i=0
	while i<len(L):
		resultat.append(L[i]+L[i+1]*2+L[i+2]*4)
		i+=3
	resultat.reverse()
	resultat=''.join(resultat)
	return resultat
def dix_vers(n1,a,Tuple):
	p=[]
	n1=int(n1)
	rest=0
	while n1:
		rest=n1%a
		n1=int(n1/a)
		if rest>=10:
			for t,v in Tuple.items():
				if v==rest:
					p.append(t)
		else:
			p.append(str(rest))
			
	p.reverse()
	p=''.join(p)
	return p

def seize_10(l,Tuple):
	 L=[]
	 for t in l:
	 	if t in Tuple:
	 		L.append(Tuple[t])
	 	else:
	 		L.append(int(t))
	 k=vers_dix(16,L)
	 return k

def vers_dix(a,l):
	resultat,i,L=0,0,[]
	for t in l:
		L.append(int(t))		
	while i<len(L):
	 		resultat+=int(L[i]*pow(a,len(L)-i-1))
	 		i+=1
	return resultat