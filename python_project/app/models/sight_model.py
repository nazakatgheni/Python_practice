from app.config.mysqlconnection import connectToMySQL
from app.models.user_model import User

class Sight:
    db = 'sasquatch_db'
    
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.date_of_siting = data['date_of_siting']
        self.description = data['description']
        self.num_of_sas = data['num_of_sas']
        self.user_id = data.get('user_id')
        self.first_name = data.get('first_name', '')
        self.last_name = data.get('last_name', '')
        
        self.likes = []
        self.poster = None
        
        if 'users.id' in data:
            self.poster = User({
                'id': data['users.id'],
                'first_name' : data['first_name'],
                'last_name' : data['last_name'],
                'email' : data['email'],
                'password' : data['password'],
            })
        
        
    # @classmethod
    # def get_one_sight(cls, id):
    #     query = """
    #         SELECT *
    #         FROM sasquatch_db.sights
    #         WHERE sights.id = %(id)s
    #     """
    #     results = connectToMySQL(cls.db).query_db(query, {'id':id})
        
    #     return cls(results[0]) if results else None
    
    @classmethod
    def get_one_sight(cls, sight_id):
        query = """
            SELECT sights.*, users.first_name, users.last_name
            FROM sights
            LEFT JOIN users ON sights.user_id = users.id
            WHERE sights.id = %(id)s
        """
        data = {'id': sight_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0]) if results else None
    
    
    # @classmethod
    # def get_all_sights(cls):
    #     query = """
    #         SELECT *
    #         FROM sasquatch_db.sights;
    #     """
    #     results = connectToMySQL(cls.db).query_db(query)
    #     return [cls(data) for data in results]
    
    @classmethod
    def get_all_sights(cls):
        query = """
            SELECT sights.*, users.first_name, users.last_name
            FROM sights
            LEFT JOIN users ON sights.user_id = users.id;
        """
        results = connectToMySQL(cls.db).query_db(query)
        
        sights = []
        for row in results:
            sight = cls(row)
            sight.user = {
                'first_name': row['first_name'],
                'last_name': row['last_name']
            }
            sights.append(sight)
        
        return sights
    
    @classmethod
    def create_sight(cls, data):
        query = """
            INSERT INTO sights
            (location, date_of_siting, description, num_of_sas, user_id)
            VALUES
            (%(location)s,%(date_of_siting)s, %(description)s, %(num_of_sas)s, %(user_id)s)
        """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update_sight(cls, data):
        query = """
        UPDATE sights
        SET location = %(location)s, date_of_siting = %(date_of_siting)s, description = %(description)s, num_of_sas = %(num_of_sas)s
        WHERE id = %(id)s 
        """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_sight(cls, id):
        query = """
            DELETE
            FROM sights
            WHERE id = %(id)s
        """
        return connectToMySQL(cls.db).query_db(query, {'id':id})

    
# from app.config.mysqlconnection import connectToMySQL
# from app.models.user_model import User


# class Sight:
#     db = 'sasquatch_db'
    
#     def __init__(self, data):
#         self.id = data['id']
#         self.location = data['location']
#         self.date_of_siting = data['date_of_siting']
#         self.description = data['description']
#         self.num_of_sas = data['num_of_sas']
        
#         self.likes = []
#         self.poster = None
        
        
#         if 'users.id' in data:
#             self.poster = User({
#                 'id': data['users.id'],
#                 'first_name' : data['first_name'],
#                 'last_name' : data['last_name'],
#                 'email' : data['email'],
#                 'password' : data['password'],
#             })
        
        
#     @classmethod
#     def get_one_sight(cls, id):
#         query = """
#             SELECT *
#             FROM sasquatch_db.sights
#             WHERE sights.id = %(id)s
#         """
#         results = connectToMySQL(cls.db).query_db(query, {'id':id})
        
#         return cls(results[0]) if results else None
    
#     @classmethod
#     def get_all_sights(cls):
#         query = """
#             SELECT *
#             FROM sasquatch_db.sights;
#         """
#         results = connectToMySQL(cls.db).query_db(query)
#         return [cls(data) for data in results]
    
#     @classmethod
#     def create_sight(cls, data):
#         query = """
#             INSERT INTO sights
#             (location, date_of_siting, description, num_of_sas, user_id)
#             VALUES
#             (%(location)s,%(date_of_siting)s, %(description)s, %(num_of_sas)s, %(user_id)s)
#         """
        
#         return connectToMySQL(cls.db).query_db(query, data)
    
#     @classmethod
#     def update_sight(cls, data):
#         query = """
#         UPDATE sight
#         SET location = %(location)s, date_of_siting = %(date_of_siting)s,  description = %(description)s, num_of_sas = %(num_of_sas)s
#         WHERE id = %(id)s 
#         """
#         return connectToMySQL(cls.db).query_db(query, data)
    
#     @classmethod
#     def delete_sight(cls, id):
#         query = """
#             DELETE
#             FROM sights
#             WHERE id = %(id)s
#         """
#         return connectToMySQL(cls.db).query_db(query, {'id':id})
    
    