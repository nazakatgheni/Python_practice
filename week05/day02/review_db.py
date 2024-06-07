class Todo:
    
    def __init__(self, data):
        self.id = data['id'],
        self.text = data['text']

        self.tasks = []
        
        
    # it will print whatever you tell it to
    # this means when we print the object that is created from this class instead of saying some weird number and letters
    # we will see it in a minute once i instantiate the instance of Todo class
    # its helpful when we use print to debug
    def __str__(self):
        return self.text


class Task: 
    
    def __init__(self, data):
        self.id = data['id']
        self.description = data['description']

    def __str__(self):
        return self.description
    

todo_data = {
    'id': 1,
    'text': "Todo 1"
}

todo = Todo(todo_data)
# print(todo)

todos_data =[{
                'id': 1,
                "text": "Todo 1",
                
                'tasks.id': 1,
                "tasks.description": "Task1"
            },
            {
                'id': 1,
                'text': 'Todo 1',
                
                'tasks.id': 2,
                "tasks.description": "Task2"
                }]

todo = Todo(todos_data[0])

for item in todos_data:
    print(item)
    todo.tasks.append(Task({
        'id': item['tasks.id'],
        'description': item['tasks.description']
    }))
    
print(todo.tasks[1].description)