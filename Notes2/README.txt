To run
export FLASK_APP=web_app_sqlalchemy

flask db init
flask db migrate
flask db upgrade

Create an author at http://localhost:5000/get_authors

Now create a note from http://localhost:5000/get_authors at http://localhost:5000/notes select the author from one created above, this should create the relationship, check add_note function

Now home page should display all notes with their authors

If you go to authors page and click on any other it should give notes written by that author, this is done with get_author_notes
