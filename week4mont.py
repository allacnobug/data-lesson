import random
S=2
N=100000
c=0
for x in range(N):
	a=random.uniform(0.0,1.0)
	b=random.uniform(0.0,2.0)
	fa=a**2+a**3
	if b<fa:
		c=c+1
print(c/N*S)
