db = None

class User(object):
    def __init__(self, age, occupation, gender):
        self.age = age
        self.occupation = occupation
        self.gender = gender

    @staticmethod
    def get(user_id):
        user = db.users.find_one({"_id": user_id})
        return User(user['age'], user['occupation'],
                user['gender'])

    def __str__(self):
        return "%s %s, age %d"%(self.gender,
                self.occupation, self.age)

