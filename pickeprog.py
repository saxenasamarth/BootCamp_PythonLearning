import pickle
dc1 ={"Apple": 1, "Oranges": 2}
dc2 ={"Car": 2, "Bike":1}

dict={}
dict["Fruits"]=dc1
dict["Vehicle"]=dc2

out=dict
f=open("conf", "wb")
pickle.dump(out, f)

f=open("conf", "rb")
x= pickle.load(f)
print(x)

