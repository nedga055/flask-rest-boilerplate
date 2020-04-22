from ..models.employee import Employee

def get_user_by_id(user_id):
    '''
    Retreives a particular user by their user ID.

    Args:
        user_id:
            An int that specifies the user_id.
    
    Returns:
        An instance of the User model.
    '''
    return Employee.query.filter_by(BrowserID=browser_id).first()

def get_all_employees():
    ''' Gets all users in the users table. '''
    return [employee.json() for employee in Employee.query.all()]