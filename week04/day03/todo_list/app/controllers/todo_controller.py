from app import app
from flask import Flask, render_template, redirect, request

from app.models.todo_model import Todo 
#this line of code will import todo class in models

#make sure u imported controller to the server.py

#read
@app.route('/')
def home():
    return render_template('home.html', todos = Todo.get_all_todos())

#read
@app.route('/todo/<int:id>')
def view_todo(id):
    return render_template('view.html', todo = Todo.get_one_by_id(id))

#create
@app.route('/todo/add')
def get_add_todo_form():
    return render_template('add.html')



#request and redirect 
#both routes should be same
#create
@app.route('/todo/add',methods=['POST'])
def add_todo():
    new_todo = request.form
    Todo.create_todo(new_todo) #always redirect when methods = Post
    return redirect('/')

#update
@app.route('/todo/update/<int:id>')
def get_update_todo_form(id):
    return render_template('update.html', todo = Todo.get_one_by_id(id))


#update
@app.route('/todo/update', methods=["POST"])
def update_todo():
    form = request.form
    #if we say application is stateless it means it got no memory
    
    Todo.update_todo(form)
    
    return redirect('/')


#  reset session
@app.route('/todo/reset')
def reset():
    pass


# delete
@app.route('/todo/delete/<int:id>')
def delete_todo(id):
    Todo.delete_todo(id)
    return redirect('/')


# we display throw the controller