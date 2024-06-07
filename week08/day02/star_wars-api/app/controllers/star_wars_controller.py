from app import app
from flask import Flask, render_template, redirect, request, flash, session
import requests
import json




api_url = 'https://swapi.dev/api'

@app.route('/hello')
def hello():
    return{
        "greeting_type": "Welcome",
        "greeting_text": "Hello World!"
    }


@app.route('/')
def dashboard():
    response = requests.get('https://swapi.dev/api/people')
    # print(response.text)
    people_response = json.loads(response.text)
    # print(people_response)
    people = people_response['results']
    print(people)
    
    # for index, person in enumerate(people):
    #     person['id'] = index + 1
    
    for i in range(len(people)):
        people[i]['id'] = i + 1

    return render_template('dashboard.html', people = people)


@app.route('/people/<int:id>')
def get_person(id):
    response = requests.get(f'{api_url}/people/{id}')
    
    person = json.loads(response.text)
    print(person)
    return render_template('people.html', person = person)