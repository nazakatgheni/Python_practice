from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello_world.html')


@app.route('/hello/<string:name>/<int:age>')
def hello_user(name,age):
    return render_template('hello_user.html', age=age, name=name)


@app.route('/user/get/<int:id>')
def get_user(id):
    user = {
        'id': 3,
        "first_name":'Amy',
        'email':'awinehouse@gmail.com'
    }
    
    #list
    items = ['apple', 'banana', 'berries']
    
    #
    users = [
    {
        'id': 1,
        'first_name': 'Wilma',
        'email_address': 'wilma@bedrock.com'
    },
    {
        'id': 2,
        'first_name': 'Barney',
        'email_address': 'barney@bedrock.com'
    },
    {
        'id': 3,
        'first_name': 'Betty',
        'email_address': 'betty@bedrock.com'
    }
]
    
    return render_template('templates_demo.html', user=user, items=items, users= users)





if __name__ == "__main__":
    app.run(debug=True)