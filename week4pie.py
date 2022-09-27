import random
S=1
N=1000000
c=0
for x in range(N):
	a=random.uniform(0.0,1.0)
	b=random.uniform(0.0,1.0)
	if a**2+b**2<=1:
		c=c+1
print(4*c/N*S)

#arctan1=pi/4
result=0
for x in range(10000):
	a=2*x+1
	b=(-1)**x*1/a*1**a
	result+=b
print(result*4)

pi=0
for x in range(100):
	pi+=1/pow(16,x)*(4/(8*x+1)-2/(8*x+4)-1/(8*x+5)-1/(8*x+6))
print(pi)
