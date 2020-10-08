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
