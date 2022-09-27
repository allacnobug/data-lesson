import random
c=int(input())

g=0.0
while g**2<c:
	if(g+1)**2<c:
		g=g+1
	else:
		break
while abs(g**2-c)>0.0001:
	g=g+0.00001
print(g)	

mmin=0
mmax=c
g=(mmax+mmin)/2
while abs(g**2-c)>0.0001:
	if g**2<c:
		mmin=g
	elif g**2>c:
		mmax=g
	g=(mmin+mmax)/2	
print(g)		

g=c/2
while abs(g**2-c)>0.0001:
	g=(g+c/g)/2	
print(g)
