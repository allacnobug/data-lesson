result=0
for x in range(1,101):
	if x%2!=0:
		print(x,end=" ")
		if x<=50:
			result+=x
print("\n",result)		
