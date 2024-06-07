from app import app
from app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask import flash
import re

# Filter string
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    
    dB = 'todos2'
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email_address = data['email_address']
        self.password = data['password']

    #! Create - Register
    @classmethod
    def register_user(cls, data):
        bcrypt = Bcrypt(app)
        query = """
            INSERT INTO 
                users 
            (first_name, last_name, email_address, password) 
            VALUES
            (%(first_name)s, %(last_name)s, %(email_address)s, %(password)s)
        """
        # before adding bcrypt
        # return connectToMySQL(cls.dB).query_db(query, data)
        return connectToMySQL(cls.dB).query_db(query, {
            **data, # this is spread operator
            "password": bcrypt.generate_password_hash(data['password'])
        })
        
    
    @classmethod
    def get_by_email(cls, email_address):
        query = """
            SELECT *
            FROM users
            WHERE email_address = %(email_address)s
        """
        results = connectToMySQL(cls.dB).query_db(query, {'email_address':email_address})
        
        #? Check to make sure something was loaded
        if not results:
            return None
        
        return cls(results[0])
    
    @staticmethod
    def validate_registration(registration_form):
        #blacklisting
        is_valid = True
        
        #?check if user exists 
        if User.get_by_email(registration_form['email_address']):
            is_valid = False
            flash("Email already exist", "registration")
        
        #? Check First name and last name
        if len(registration_form['first_name']) < 3:
            is_valid = False
            flash("First name must be at least 3 characters", "registration")
            
        if len(registration_form['last_name']) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters", "registration")
        
        #? Check password length
        if len(registration_form['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters", "registration")
        
        #? Check password and confirm password matches
        if registration_form['password'] != registration_form['confirm_password']:
            is_valid = False
            flash("Password must match", "registration")
        
        if len(registration_form['email_address']) == 0:
            is_valid = False
            flash("Email is required", "registration")
        
        if not EMAIL_REGEX.match(registration_form['email_address']):
            is_valid = False
            flash("Invalid email address", "registration")
        
        if is_valid:
            flash("Thanks for registering", 'registration')
        
        return is_valid