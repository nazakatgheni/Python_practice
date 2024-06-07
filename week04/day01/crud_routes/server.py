import random
from datetime import datetime
from flask import Flask, render_template, session, redirect,request
#redirect is same as navigate in mern

app = Flask(__name__)
app.secret_key = "my_secret_key"


# READ
@app.route('/')
def home():
    
    if not session.get('todos'):
        session['todos'] = [
            {
                "id": random.randint(1,1000000),
                "text": "Todo 1",
                "description": "Feed the cat, to dog",
                "created_at": datetime.now()
            }
        ]
    
    return render_template('home.html', todos=session['todos'])


@app.route('/todo/<int:id>')
def view_todo(id): # make sure when u naming u have one verb here
    # for todo in session['todos']:
    #     if todo['id'] == id:
    #         print("found")

#a list comprehension
    found_todo = [todo for todo in session['todos'] if todo['id'] == id][0]
    return render_template('view.html', todo = found_todo)


#render form
@app.route('/todo/add')
def get_add_todo_form():
    return render_template("add.html")


#request and redirect 
#both routes should be same
@app.route('/todo/add',methods=['POST'])
def add_todo():
    new_todo = request.form
    todos = session.get('todos') # we don't have backend yet that's why we use session
    todos.append(
        {
                "id": random.randint(1,1000000),
                "text": new_todo['text'],
                "description": new_todo['description'],
                "created_at": datetime.now()
            }
    )
    session['todos'] = todos #save todo
    return redirect('/')

@app.route('/todo/update/<int:id>')
def get_update_todo_form(id):
    #find todo by id
    found_todo = [todo for todo in session['todos'] if todo['id'] == id][0]
    if found_todo is None:
        return "Todo not found, 404"
    return render_template('update.html', todo = found_todo)

@app.route('/todo/update', methods=["POST"])
def update_todo():
    updated_data = request.form
    todos = session.get('todos')

    #find and update specific todo
    for todo in todos:
        if todo['id'] == int(updated_data['id']):
            todo['text'] = updated_data['text']
            todo['description'] = updated_data['description']
            break
    #save the update todos back to the session
    session['todos'] = todos
    return redirect('/')

#  reset session
@app.route('/todo/reset')
def reset():
    session.clear()
    return redirect('/')

# delete
@app.route('/todo/delete/<int:id>')
def delete_todo(id):
    #retrieve the list of todo from the session
    todos = session.get('todos')
    # filter the todo with id
    found_todo = [todo for todo in todos if todo['id'] != id]
    session['todos'] = found_todo
    return redirect('/')



if __name__ == "__main__": # Ensure this file is being run directly and not from a different module
    app.run(debug=True) # Run the app in debug mode.
