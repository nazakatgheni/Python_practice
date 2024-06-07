from app.config.mysqlconnection import connectToMySQL
from app.models.task_model import TaskModel

#we're Encapsulating the 


class Todo:
    db = 'todos2' # this should match the db name that we named 
    
    #constructor
    def __init__(self,data): # this data will be a dictionary
        self.id = data['id']
        self.text = data['text']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.tasks = []
        

# read all
    @classmethod
    def get_all_todos(cls):
        query = """
            SELECT
                *
            FROM
                todos
        """
        
        result = connectToMySQL(cls.db).query_db(query)
        
        rows = []
        # each result is dictionary 
        for result in result:
            rows.append(cls(result)) # instantiate todo dictionary
        
        return rows

#read one
    @classmethod
    def get_one_by_id(cls, id):
        query = """
        SELECT 
            *  
        FROM 
            todos
        WHERE
	        id = %(id)s 
        """
        
        return cls(connectToMySQL(cls.db).query_db(query, {'id':id})[0]) # we're sepecifying we only need one line with index 0

#read a single todo with tasks 
#? LEFT JOIN 
    @classmethod
    def get_one_by_id_1_to_many(cls,id): #todos2
        query = """
        SELECT
        * 
        FROM
        todos
        LEFT JOIN tasks ON tasks.todo_id = todos.id
        WHERE
        todos.id = %(id)s
        """
        #      we're having a list of dictionary
        results = connectToMySQL(cls.db).query_db(query, {'id':id})

        if results:
            # create instance of todo that we want to populate 
            #grabbing the first line from the results
            todo = cls(results[0])
            
            for result in results:
                task = TaskModel({
                    'id' : result['tasks.id'], # we're refering to tasks table
                    'description' : result['tasks.description']
                })
                print(task)
                todo.tasks.append(task)
            return todo
        return None






#update
    @classmethod
    def update_todo(cls, data):
        query = """
        UPDATE 
            todos
        SET 
            text = %(text)s,
            description = %(description)s
        WHERE
	        id = %(id)s 
        """
        
        return connectToMySQL(cls.db).query_db(query, data)
    
#create
    @classmethod
    def create_todo(cls, data):
        query = """
        INSERT INTO
	            todos
        (text, description)
        VALUES
        (%(text)s, %(description)s)
        """
        return connectToMySQL(cls.db).query_db(query, data)

#delete
    @classmethod
    def delete_todo(cls, id):
        query = """
            DELETE
            FROM
                todos
            WHERE
                id = %(id)s
        """
        return connectToMySQL(cls.db).query_db(query, {'id':id})
