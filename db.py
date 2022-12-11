import json

class Database:

    def insert(self,name,email,password):
        with open('user.json','r') as rf:
            users = json.load(rf)

            if email in users:
                return 0
            else:
                users[email] = [name,password]
        with open('user.json','w') as wf:
            json.dump(users,wf)
            return 1