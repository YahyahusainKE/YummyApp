userdata = {}


class User:
    '''stores information  of users input  '''

    def __init__(self, first_name,last_name, email, password, cofirm):
        self.First_name = first_name
        self.Last_name = last_name
        self.Email = email
        self.Password = password
        self.Confirm = cofirm
        userdata.update({'FirstName': self.first_name, 'LastName': self.last_name, 'Password': self.password,
                         'Confirm': self.cofirm})

