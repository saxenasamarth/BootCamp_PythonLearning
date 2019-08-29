f = open("Python.txt", "w")
f.write("Hello , this is a python output")
f.close()

f =open("Python.txt", "r")
strlist = f.readlines()
print(strlist[0].split(","))
f.close()

f = open("Python.txt", "a")
f.write("\n Adding this to output, hurray")
f.close()

with open("Python.txt", "a") as f:
		f.write("\n hello again \n")

