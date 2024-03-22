from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
from pymongo.errors import ConnectionFailure
import urllib.parse


class Database:

    def __init__(self) -> None:
        self.client = None
        self.db = None

    def init_db(self):
        try:
            username = urllib.parse.quote_plus("user")
            password = urllib.parse.quote_plus("secret")
            self.client = MongoClient(
                "mongodb://%s:%s@localhost" % (username, password)
            )
            self.db = self.client["foracs"]
            print("MONGO DATABASE Connected successfully!!!")
        except ConnectionFailure as e:
            print("Could not connect to MongoDB   -- ", e)

    def get_one_by_ObjId(self, post_id: str):
        # Convert from string to ObjectId:
        document = self.db.employees.find_one({"_id": ObjectId(post_id)})
        print(document)

    def insert_one(self, employ_obj: dict):
        post_id = self.db.employees.insert_one(employ_obj).inserted_id
        print(f"Employee with id : {post_id} inserted to db")

    def find_one_by_name(self, name: str):
        one = self.db.employees.find_one({"name": name})
        print(one)


employeee = {
    "name": "Fred",
    "position": "Test Leader",
    "text": "My first db post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}


db_obj = Database()
db_obj.init_db()
db_obj.insert_one(employeee)
db_obj.find_one_by_name('Fred')








