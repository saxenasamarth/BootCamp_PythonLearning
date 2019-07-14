from pymongo import MongoClient
from bson.objectid import ObjectId

client=MongoClient()
db=client["MiniAmazon"]


def uname_exists(uname):
	if db.users.find_one({"username":uname})!=None:
		return True
	else:
		return False

def check_passw(uname, password):
	user_detail=db.users.find_one({"username":uname}) # as we want to use the response of this find on DB multiple time, we have saved in variable
	if user_detail!=None:
		if user_detail["passw"]==password:
			return user_detail["type"]
		else:
			return "Wrong password"


def createUser(userProfile_dict):
	db.users.insert(userProfile_dict)


#product related function

def add_ProdToList(pname,pprice,pdesc,uname):
	if db["Products"].find_one({"product_name":pname})==None:
		db["Products"].insert({"product_name":pname,"product_price":pprice,"product_desc":pdesc,"product_seller":uname})
		return True
	else:
		return False

def getAllProducts():
	all_products=db["Products"].find({})
	prod_list=[]
	for x in all_products:
		prod_list.append(x)
	return prod_list

def deleteProduct(product_name):
	db["Products"].remove({"product_name":product_name})

def getProductInfo(item_id):
	itemdetails_list=[]
	print(item_id)
	item_detail=db["Products"].find_one({"_id":ObjectId(item_id)})
	print(item_detail)
	return item_detail



#cart functions
def addtoCart(p_id,username):
	userInfo=db["users"].find_one({"username":username})
	if userInfo!=None:
		if "cart" in userInfo:
			cart_dict=userInfo["cart"]
		else:
			cart_dict={}
	print(cart_dict)

	if p_id in cart_dict:
		cart_dict[p_id]+=1
		db["users"].update({"username":username},{'$set':{"cart":cart_dict}})
		mycart=db["users"].find_one({"username":username})
		return mycart["cart"]

	else:
		cart_dict[p_id]=1
		db["users"].update({"username":username},{'$set':{"cart":cart_dict}})
		mycart=db["users"].find_one({"username":username})
		return mycart["cart"]

def getCart(username):
	mycart=db["users"].find_one({"username":username})
	return mycart["cart"]



