from flask import Flask,render_template,request,url_for,redirect,session,jsonify
from models.model import *
#print(dir(models.model))
app =Flask(__name__)
app.secret_key = 'hello'


@app.route("/")
def home_page():
	session.clear()
	return render_template("home.html",title ="home")

@app.route("/about")
def about_page():
	return render_template("about.html",title="about")

@app.route("/contact")
def contact_page():
	return render_template("contact.html")

@app.route("/signup", methods=['POST'])
def signup_page():
	print(request.form)
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
			return redirect(url_for("home_page"))
		else:
			return "passwords do not match"


app.run(debug=True)