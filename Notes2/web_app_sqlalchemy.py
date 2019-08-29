from flask import Flask, redirect, url_for, request, render_template, jsonify, flash, send_from_directory
import datetime
import pickle, random
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from werkzeug import secure_filename
from celery import Celery
import os
import time
import requests
from celery import Celery
from celery.schedules import crontab

app = Flask(__name__) # object of Flask instantiation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.secret_key="hello"


app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'



CELERYBEAT_SCHEDULE = {'test-celery': {'task': 'bg_task','schedule': 50.0,}}

app.config['CELERYBEAT_SCHEDULE'] = CELERYBEAT_SCHEDULE

def create_celery(app):
   celery = Celery(app.import_name,
                   backend=app.config['CELERY_RESULT_BACKEND'],
                   broker=app.config['CELERY_BROKER_URL'])
   celery.conf.update(app.config)
   TaskBase = celery.Task

   class ContextTask(TaskBase):
       abstract = True

       def __call__(self, *args, **kwargs):
           with app.app_context():
               return TaskBase.__call__(self, *args, **kwargs)
   celery.Task = ContextTask
   return celery

celery = create_celery(app)


from flask_migrate import Migrate
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
db.init_app(app)
migrate = Migrate(app, db)
migrate.init_app(app, db, render_as_batch=True)
with app.app_context():
	db.create_all()

default_image="default.png"
image_path = os.getcwd()+"/images/"
app.config['UPLOAD_FOLDER']=image_path
	
class Author(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	notes = db.relationship('Note', backref='author', lazy=True)
	image = db.Column(db.String(200), default=default_image, nullable=True)	
	
class Note(db.Model):
	id = db.Column('id', db.Integer, primary_key = True)
	note = db.Column(db.String(1000))
	created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	updated_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)	
	author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)		
	
@app.route('/notes') 
def notes():
    authors = Author.query.all()
    return render_template("add_note.html", authors=[x for x in authors])					

@app.route('/')
@app.route('/get_notes',methods = ['GET'])
def get_notes():
	if request.method == 'GET':
		notes = Note.query.all()
		return render_template("all_notes.html", notes=[x for x in notes])

@app.route('/get_author_notes',methods = ['GET'])
def get_author_notes():
	if request.method == 'GET':
		name = request.args["name"]
		notes = Note.query.join(Author).filter(Author.name==name)
		return render_template("all_notes.html", notes=[x for x in notes])		
		
@app.route('/get_authors',methods = ['GET'])
def get_authors():
	if request.method == 'GET':	
		authors = Author.query.all()
		return render_template("all_authors.html", authors=[x for x in authors])		
		
@app.route('/add_note',methods = ['POST'])
def add_note():
	if request.method == 'POST':
		if "note" in request.form:
			n = Note(note=request.form["note"])
			author_name = request.form["comp_select"]
			print("Author", author_name)
			author = Author.query.filter_by(name=author_name).first()
			author.notes.append(n)
			db.session.add(n)
			db.session.commit()
			flash('Added note')
			return redirect(url_for('get_notes'))
		else:
			return "No data given"
			
@app.route('/render_add_author',methods = ['GET'])
def render_add_author():
	return render_template("add_author.html")						
			
@app.route('/add_author',methods = ['POST'])
def add_author():
	if request.method == 'POST':
		print(request.files, request.form)
		if 'file' in request.files and request.files['file']!='':
			f = request.files['file']
			filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
			print(filepath)
			f.save(filepath)
			a = Author(name=request.form["name"], image=f.filename)
		else:
			a = Author(name=request.form["name"])
		db.session.add(a)
		db.session.commit()
		return redirect(url_for('get_authors'))		
			
@app.route('/update_note',methods = ['POST'])
def update_note():
	if request.method == 'POST':
		if "note" in request.form:
			note_text = request.form["note"]
			fetch_note = Note.query.filter_by(id=request.form["id"]).first()
			fetch_note.note = note_text
			fetch_note.updated_time = datetime.datetime.utcnow()
			db.session.commit()
			return redirect(url_for('get_notes'))
		else:
			return "No data given"

@app.route('/delete_note',methods = ['POST'])
def delete_note():
	if request.method == 'POST':
		if "id" in request.form:
			Note.query.filter_by(id=request.form["id"]).delete()
			db.session.commit()
			return redirect(url_for('get_notes'))
		else:
			return "No data given"			
						
@app.route('/modify_note') 
def modify_note():
    return render_template("update_note.html",note=request.args["note"], id=request.args["id"])

@app.route('/images/<filename>')
def send_file(filename):
   return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@celery.task 
def dummy_task(a,b):
	time.sleep(1)
	print(a+b)

@celery.task
def background_task():
    url = "https://www.alfaromeousa.com/content/dam/alfausa/2019/Giulia/Desktop/2019-AlfaRomeo-VLP-Giulia2019-AlfaRomeo-VLP-Giulia-SDP-Gallery-3.jpg.image.1440.jpg"
    print(url)
    open('images/federer.jpg', 'wb').write(requests.get(url, allow_redirects=True).content)
    return "Done"

@app.route('/get_image',methods = ['POST'])
def get_image():
    background_task.delay()
    return redirect(url_for("get_notes"))


@celery.task(name='bg_task')
def change_bg():
    url_list = ["https://www.alfaromeousa.com/content/dam/alfausa/2019/Giulia/Desktop/2019-AlfaRomeo-VLP-Giulia2019-AlfaRomeo-VLP-Giulia-SDP-Gallery-3.jpg.image.1440.jpg","data:image/jpeg;base64,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","https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2019-lamborghini-urus-lead-1545150864.jpg"]    
    url = random.choice(url_list)
    open('images/federer.jpg', 'wb').write(requests.get(url, allow_redirects=True).content)


	
if __name__ == '__main__':
   app.run(debug=True)