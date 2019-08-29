a = []
b = []
num=1
nume=1
count=0
for i in range(6):
	for j in range(1,7):
		a.append(num)
		num+=1

for m in range(6):
	for n in range(1,8):
		b.append(nume)
		nume+=1

print(a)
print("\n")
print(b)


if len(a)==len(b):
	print("length same.. comparing further", end="\n ")
	while (count<len(a)):
		if a[count]==b[count]:
			count+=1	
		else:
			print("Matrice are not same")
			break
	print("Matrice Matched")
else:
	print("length not same")

