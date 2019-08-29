a="Emma is a good developer. Emma is also a writer"
l=a.split()
myDict ={}


for i in l:
	if i not in myDict:
		myDict[i]=1

	else:
		myDict[i]+=1
print(myDict)
