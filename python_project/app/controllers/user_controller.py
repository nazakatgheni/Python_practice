from app import app
from app.models.user_model import User
from flask import Flask, render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt

from app.models.sight_model import Sight


bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('/user/home.html')

@app.route('/user/register', methods = ["POST"])
def register():
    
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password":request.form['password'],
    }
    
    if User.validate_registration(request.form):
        User.register(data)
        return redirect('/')
    return redirect('/')

@app.route('/user/login', methods = ['POST'])
def login():
    form = request.form
    
    user = User.get_by_email(form.get('email')) #form['email']
    
    if not user or not bcrypt.check_password_hash(user.password, request.form['password']):
        
        flash("Invalid Credentials", 'login')
        return redirect('/')
    
    session['user_id'] = user.id # session
    
    return redirect('/user/dashboard')

@app.route('/user/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    user = User.get_one_by_id(session['user_id'])
    sights = Sight.get_all_sights()
    
    for sight in sights:
        # Check if the user is logged in and is the owner of the sight
        sight.can_edit = (sight.user_id == session['user_id'])
        
        # if 'user_id' in session and sight.user_id == session['user_id']:
        #     sight.can_edit = True
        # else:
        #     sight.can_edit = False
        
    
    return render_template('/user/dashboard.html', sights = sights, user = user)

@app.route('/user/logout')
def logout():
    session.clear() 
    return redirect('/')
    
