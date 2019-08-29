a ="pineapple"
dict={}
for i in range(len(a)):
	if a[i] not in dict:
		dict[a[i]]=1
	else :
		dict[a[i]]+=1

print(dict)
