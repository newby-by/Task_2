from faker import Faker

BASE_URL = 'https://stellarburgers.education-services.ru/api'
REGISTER_URL = BASE_URL + '/auth/register'
LOGIN_URL = BASE_URL + '/auth/login'


class UserData:

    def __init__(self, locale='en_US'):
        self.faker = Faker(locale)
        self.user = {
            'email': None,
            'password': None,
            'name': None
        }

    @property
    def email(self):
        return self.faker.email()

    @property
    def password(self):
        return self.faker.password()

    @property
    def name(self):
        return f'{self.faker.name()}{self.faker.random_int(min=100, max=1000)}'

    @property
    def with_all_data(self):
        self.user['email'] = self.email
        self.user['password'] = self.password
        self.user['name'] = self.name
        return self.user

    @property
    def without_email(self):
        self.user['password'] = self.password
        self.user['name'] = self.name
        return self.user

    @property
    def without_password(self):
        self.user['email'] = self.email
        self.user['name'] = self.name
        return self.user

    @property
    def without_name(self):
        self.user['email'] = self.email
        self.user['password'] = self.password
        return self.user

    @staticmethod
    def data_for_login(user_data):
        return {
            'email': user_data.get('email'),
            'password': user_data.get('password'),
        }

    @staticmethod
    def change_email(user_data):
        user = user_data['email'].split('@')
        user[0] = user[0] + '123'
        user_data['email'] = "".join(user)
        return user_data
    
    @staticmethod
    def change_password(user_data):
        user_data['password'] = user_data['password'] + '123'
        return user_data
