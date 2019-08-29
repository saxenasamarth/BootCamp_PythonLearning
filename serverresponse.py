from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/hello')
def helloworld():
	return 'Hello samarth'

@app.route('/hello/<x>')
def hellox(x):
	return "Hello {}".format(x)

#redirect example
@app.route("/hellor/<v>")
def hello_version(v):
	print(v)
	if v=='v1':
		return redirect(url_for("hello"))
	else:
		return redirect(url_for("helloworld"))


#getting disctionary as the input from URL
@app.route("/hello_name",methods=['GET'])
def get_name():
	if request.method=='GET':
		print(request.args)
		if "name" in request.args:
			name=request.args['name']
			return "Hello {}".format(name)
		else:
			return "no data found"


# for the below you should have your HTML in a standard folder named "Templates"
@app.route("/hello_html")
def hello_html():
	return render_template("hello.html")

@app.route('/hello_html/<n>')
def hello_name_html(n):
	return render_template("hello_name.html",name=n)

@app.route('/notes')
def notes():
	return render_template("add_note.html")


if __name__=='__main__':
	app.run(debug=True)



