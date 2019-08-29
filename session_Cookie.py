from flask import Flask,render_template,request,url_for,redirect,session,jsonify
app = Flask(__name__)
app.secret_key = 'hello'
@app.route('/login',methods=['POST','GET'])
def login():
    session["usernamex"] = "hii"
    return "Logged in"
    
@app.route('/nologin',methods=['POST','GET'])
def nologin():
    return "Not Logged in"    
@app.route('/access')
def access():
    print(session)
    if "usernamex" in session:
        return "Accessible"
    return redirect(url_for('nologin'))
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
    
app.run()
