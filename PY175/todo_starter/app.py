from flask import (
    flash,
    Flask, 
    redirect, 
    render_template, 
    request,
    session,
    url_for
)

from utils import *
from uuid import uuid4
from werkzeug.exceptions import NotFound


app = Flask(__name__)
app.secret_key = "Matsuyama_01"

@app.before_request
def initialize_session():
    if 'lists' not in session:
        session['lists'] = []

@app.route("/")
def index():
    return redirect(url_for('get_lists'))

@app.route("/lists/new")
def add_todo_list():
    return render_template('new_list.html')

@app.route("/lists", methods = ['POST'])
def create_list():
    title = request.form['list_title'].strip()
    error = error_for_list_title(title, session['lists'])
    if error:
        flash(error, "error")
        return render_template('new_list.html', title = title) 

    session['lists'].append({ 'id':str(uuid4()),
                                'title':title,
                                'todos':[]})
    flash("The list has been created", "success")
    session.modified = True
    return redirect(url_for('get_lists'))

@app.route("/lists")
def get_lists():
    return render_template("lists.html", lists = session['lists'])

@app.route("/lists/<list_id>", methods = ['GET', 'POST'])
def show_list(list_id):
    lst = find_list(list_id, session)
    if not lst:
        raise NotFound("The requested resource was not found.")
    return render_template('list.html', lst = lst)
    
@app.route("/lists/<list_id>/todos", methods = ['POST'])
def create_todo(list_id):
    lst = find_list(list_id, session)
    if not lst:
        raise NotFound("The requested list was not found")
    todo_title = request.form['todo'].strip()
    error = error_for_todo(todo_title)
    if error:
        flash(error, "error")
        return render_template('list.html', lst = lst)
    todo = {}
    todo['title'] = todo_title
    todo['completed'] = False
    todo['id'] = str(uuid4()) 
    lst['todos'].append(todo)
    flash("The todo has been added", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id = list_id)) 

@app.route("/lists/<list_id>/todos/<todo_id>/toggle", methods = ['POST'])
def edit_todo(list_id, todo_id):
    lst = find_list(list_id, session) 
    if not lst:
        raise NotFound("The requested list was not found")
    todo = find_todo(todo_id, lst)
    if not todo:
        raise NotFound("The requested list was not found")
    todo['completed'] = (request.form['completed'] == "True")
    flash(f"The todo status has been updated to {'completed' if todo["completed"] else 'incomplete'} ", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id = list_id)) 

@app.route("/lists/<list_id>/todos/<todo_id>/delete", methods = ['POST'])
def delete_todo(list_id, todo_id):
    lst = find_list(list_id, session) 
    if not lst:
        raise NotFound("The requested list was not found")

    todo = find_todo(todo_id, lst)
    if not todo:
        raise NotFound("The requested list was not found")
    
    delete_todo_by_id(todo_id, lst)
    flash("the do has been deleted", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id = list_id))

@app.route("/lists/<list_id>/complete_all", methods = ['POST'])
def mark_all_todos_completed(list_id):
    lst = find_list(list_id, session)
    if not lst:
        raise NotFound("The requested list was not found")
    
    mark_all_completed(lst)
    flash("All tasks has been marked as completed", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id = list_id))

@app.route("/lists/<list_id>/edit")
def edit_list(list_id):
    lst = find_list(list_id, session)
    if not lst:
        raise NotFound("The requested list was not found")
    return render_template('edit_list.html', lst = lst)

if __name__ == "__main__":
    app.run(debug=True, port=5003)