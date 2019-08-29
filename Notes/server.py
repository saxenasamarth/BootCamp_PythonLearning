from flask import Flask, render_template, request, jsonify, redirect, url_for
from note import notes
from functools import wraps
import pickle

app=Flask(__name__)


try:
	f=open("file", "rb")
	note_list=pickle.load(f)
except Exception as ex:
	print(ex)
	note_list=[]


def save_state(func):
		@wraps(func)
		def inner_func(*args,**kwargs):
			print("saving state")
			value=func(*args, **kwargs)
			filer =open("file", "wb")
			pickle.dump(note_list, filer)  # understand why i had to use notes.note_list here???????????????????
			filer.close()
			
			return value
		return inner_func


@app.route('/notes')
def notes_page():
	return render_template("add_note.html")



@app.route('/add_note',methods =["POST"])
@save_state
def add_note():
	if request.method=="POST":
		if "note" in request.form: #request.form is the summision of the form in html which has tag named notes
			note=request.form['note']
			n1=notes(note)
			note_list.append(n1)
			return redirect(url_for("getAllNotes"))
		else:
			return "No data Given"

@app.route('/')
@app.route('/get_notes', methods=['GET'])
def getAllNotes():
	if request.method=="GET":
		return render_template("all_notes.html", notes=[x.get_info() for x in note_list])

#@notes.save_state
@app.route('/modify_note')
def modify_note():
	return render_template("update_note.html",note=request.args["note"], id=request.args["id"])
	#request.args("note") is the value from note.note in all_notes.html 
	#all_notes.html has modify button for each note, that calls modify_notes url and passes note value and ID value.
	#That note and ID value is read here by using request.args(key=note). args is a dictionary


@app.route('/update_note', methods=['POST'])
@save_state
def update_notecall():
	if request.method=="POST":
		lid=int(request.form["id"])
		lnote=request.form["note"]
		for x in notes.note_list:
			if x.match_id(lid):
				x.update_note(lnote)
				return redirect(url_for('getAllNotes'))


@save_state
@app.route('/delete_note', methods=['POST'])
def delete_note():
	print("hi")
	if request.method=="POST":
		del_id=int(request.form["id"])
		print(del_id)
		for x in notes.note_list:
			if x.match_id(del_id):
				del notes.note_list[del_id-1]
				return redirect(url_for('getAllNotes'))







if __name__=='__main__':
	app.run(debug=True)
