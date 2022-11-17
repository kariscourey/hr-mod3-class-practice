from queries.client import client, dbname

class UserQueries:
    def get_all_users(self):
        db = client[dbname]
        result = list(db.users.find())
        for value in result:
            value['id'] = value['_id']
        return result

    def get_user(self, id):
        db = client[dbname]
        result = db.users.find_one({'_id': id})
        if result:
            result['id'] = result['_id']
            return result

    def create_user(self, data):
        db = client[dbname]
        result = db.users.insert_one(data.dict())
        if result.inserted_id:
            result = self.get_user(result.inserted_id)
            result['id'] = str(result['id'])
            return result

    def update_user(self, user_id, data):
        pass

    def delete_user(self, user_id):
        pass
