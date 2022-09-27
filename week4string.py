s=input()
max=1
t=1
for x in range(0,len(s)-1):
	if s[x]==s[x+1]:
		t=t+1
		if t>max:
			max=t
	else:
		t=1
print(max)
