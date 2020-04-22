from app.main.db import db

class Employee(db.Model):
    '''
    A simple employee model for illustrative purposes.
    '''
    __tablename__ = "employees"

    ID = db.Column(db.Integer, primary_key=True,)
    FirstName = db.Column(db.String(), nullable=False,)
    LastName = db.Column(db.String(), nullable=False,)
    Email = db.Column(db.String(), nullable=False,)

    def __init__(self, first_name, last_name, email):
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email

    def json(self):
        ''' Creates a JSON representation of the current instance of User. '''
        return {
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'Email': self.Email,
        }
    
    def save_to_db(self):
        ''' Saves the instance of UserModel to the database. '''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        ''' Saves the instance of UserModel to the database. '''
        db.session.delete(self)
        db.session.commit()

