from app import app
from flask import Flask, render_template, redirect, request, flash, session
from app.models.sight_model import Sight
from app.models.user_model import User



#display
@app.route('/sight/<int:sight_id>')
def display_sight(sight_id):
    if 'user_id' not in session:
        return redirect('/')
    
    sight = Sight.get_one_sight(sight_id)
    
    if not sight:
        flash("Sighting not found")
        return redirect('/user/dashboard')
    
    user = User.get_one_by_id(session['user_id'])
    return render_template('/sight/display_sight.html', sight = sight, user = user)#sight = Sight.get_one_sight(sight_id)


# @app.route('/sight/my')
# def my_sights():
    
#     if not 'user_id' in session:
#         return redirect('/')
    
#     return render_template('/sight/my_sights.html', user = User.get_one_by_id(session['user_id']))


#report a sight
@app.route('/sight/add')
def get_add_sight_form():
    
    if not 'user_id' in session:
        return redirect('/')
    
    user = User.get_one_by_id(session['user_id'])
    return render_template('/sight/report_new_sight.html', user = user)


#report a sight
@app.route('/sight/add', methods=['POST'])
def add_sight():
    if not 'user_id' in session:
        return redirect('/')
    
    Sight.create_sight({
        **request.form,
        'user_id': session['user_id'],
    })
    return redirect('/user/dashboard')


#edit a sight
@app.route('/sight/update/<int:sight_id>')
def get_update_sight_form(sight_id):
    
    if not 'user_id' in session:
        return redirect('/')
    
    return render_template('/sight/edit_sight.html', sight = Sight.get_one_sight(sight_id))


#edit a sight
@app.route('/sight/update', methods=['POST'])
def update_sight():
    if not 'user_id' in session:
        return redirect('/')
    
    Sight.update_sight(request.form)
    
    return redirect('/user/dashboard')



@app.route('/sight/delete/<int:sight_id>')
def delete(sight_id):
        Sight.delete_sight(sight_id)
        return redirect('/user/dashboard')



