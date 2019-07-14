from flask import Flask,render_template,request,url_for,redirect,session,jsonify
from models.model import *
#print(dir(models.model))
app =Flask(__name__)
app.secret_key = 'hello'


@app.route("/")
def home_page():
	#session.clear()
	#print("logged in as {0} and {1}".format(str(session["username"]),str(session["type"])))
	return render_template("home.html",title ="home")

@app.route("/about")
def about_page():
	return render_template("about.html",title="about")

@app.route("/contact")
def contact_page():
	return render_template("contact.html")

@app.route("/login", methods=["POST"])
def login_page():
	uname=request.form["username"]
	passw=request.form["password"]

	if uname_exists(uname):
		checkpass_resp=check_passw(uname, passw)
		if checkpass_resp!=None:
			session["username"]=uname
			session["type"]=checkpass_resp
			#print("logged in as {0} and {1}".format(str(session["username"]),str(session["type"])))
			return redirect(url_for("home_page"))
		else:
			return "username password not valid"
	else:
		return "username does not exist"

@app.route("/products",methods=["POST","GET"])
def product_page():
	if request.method=="POST":
		prod_name = request.form["name"]
		prod_price=request.form["price"]
		prod_desc=request.form["description"]
		#isProductAdded = add_ProdToList(prod_name,prod_price,prod_desc)
		if add_ProdToList(prod_name,prod_price,prod_desc,session["username"]) == True:
			return redirect(url_for("home_page"))
		else:
			return "Product Exists in Database, Enter New Product"
	else :
		return render_template("products.html",products=getAllProducts())

@app.route("/remove_product", methods=["POST"])
def removeProduct_page():
	if request.method=="POST":
		prod_name=request.form["name"]
		deleteProduct(prod_name)
		return redirect(url_for("product_page"))






@app.route("/signup", methods=['POST'])
def signup_page():
	#print(request.form)
	uname=request.form["username"]
	passw=request.form["password1"]
	veri_passw=request.form["password2"]
	user_type=request.form["type"]
	userProfile={}
	if uname_exists(uname):
		return "username already taken! try another one"
	else:
		if passw==veri_passw:
			userProfile["username"]=uname
			userProfile["passw"]=passw
			userProfile["type"]=user_type
			createUser(userProfile)
			session["username"]=uname
			session["type"]=user_type
			return redirect(url_for("home_page"))
		else:
			return "passwords do not match"


@app.route("/cart", methods=['POST','GET'])
def addtocart_page():
	cart=[]
	if request.method=="POST":
		product_id=request.form["id"]
		cart_items = addtoCart(product_id, session["username"])
		for keyofItem in cart_items:
			cart.append(getProductInfo(keyofItem))
			#print(cart)
		return render_template("cart.html", cart=cart)
	else:

		cart_items=getCart(session["username"])
		for keyofItem in cart_items:
			cart.append(getProductInfo(keyofItem))
			#print(cart)
		return render_template("cart.html", cart=cart)

@app.route("/logout", methods=['GET'])
def logout_page():
	session.clear()
	return "logged out, Close window, open and login again"

app.run(debug=True)