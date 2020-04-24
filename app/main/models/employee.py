from app.main.db import db

class Employee(db.Model):
    '''
    A simple employee model for illustrative purposes.
    '''
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True,)
    first_name = db.Column(db.String(), nullable=False,)
    last_name = db.Column(db.String(), nullable=False,)
    email = db.Column(db.String(), nullable=False,)

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def json(self):
        ''' Creates a JSON representation of the current instance of User. '''
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }
    
    def save_to_db(self):
        ''' Saves the instance of UserModel to the database. '''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        ''' Saves the instance of UserModel to the database. '''
        db.session.delete(self)
        db.session.commit()

