import pymongo as pym
from bson.objectid import ObjectId

#Class for MongoDB
class MongoDB:
    def __init__(self):
        self.uri = "mongodb+srv://daniel:310030067@data.b9y24.gcp.mongodb.net/p1?retryWrites=true&w=majority"

    def find_user(self, username):
        client = pym.MongoClient(self.uri)
        user = client.p1.Usuarios.find_one({'username': username})
        return user

    def insert_user(self, user):
        client = pym.MongoClient(self.uri)
        userdb = self.find_user(user['username'])
        if userdb:
            return userdb
        user['bitacora'] = []
        client.p1.Usuarios.insert_one(user)
        return user

    def insert_activity(self, activity, user_id):
        client = pym.MongoClient(self.uri)
        print('*******************')
        print(user_id)
        print(activity)
        print('*******************')
        user = client.p1.Usuarios.find_one({"_id": ObjectId(user_id)})
        #if userdb:
        #    return null
        user['bitacora'].append(activity)
        client.p1.Usuarios.update_one({"_id": ObjectId(user_id)}, {"$set": {"bitacora" : user['bitacora']}})
        return user
