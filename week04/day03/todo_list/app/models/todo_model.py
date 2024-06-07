from app.config.mysqlconnection import connectToMySQL

#we're Encapsulating the 


class Todo:
    db = 'todos_db' # this should match the db name that we named 
    
    #constructor
    def __init__(self,data): # this data will be a dictionary
        self.id = data['id']
        self.text = data['text']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


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
        
        return cls(connectToMySQL(cls.db).query_db(query, {'id':id})[0])

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
